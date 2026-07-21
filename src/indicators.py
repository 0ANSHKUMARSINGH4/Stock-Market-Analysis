"""
indicators.py
----------------
Module containing functions to compute technical indicators such as Moving Averages
and Relative Strength Index (RSI) using Pandas and NumPy.
"""

import pandas as pd
import numpy as np


def add_moving_averages(
    df: pd.DataFrame,
    short_window: int = 20,
    long_window: int = 50,
    price_col: str = "Close"
) -> pd.DataFrame:
    """
    Calculate short-term and long-term Simple Moving Averages (SMA).

    Parameters:
        df (pd.DataFrame): Input stock DataFrame containing price column.
        short_window (int): Window period for short-term MA (default: 20).
        long_window (int): Window period for long-term MA (default: 50).
        price_col (str): Column name to use for MA calculation (default: 'Close').

    Returns:
        pd.DataFrame: DataFrame with added columns `SMA_{short_window}` and `SMA_{long_window}`.
    """
    df = df.copy()
    
    short_col = f"SMA_{short_window}"
    long_col = f"SMA_{long_window}"

    df[short_col] = df[price_col].rolling(window=short_window, min_periods=1).mean()
    df[long_col] = df[price_col].rolling(window=long_window, min_periods=1).mean()

    print(f"[Indicators] Added {short_col} and {long_col} indicators.")
    return df


def add_rsi(
    df: pd.DataFrame,
    period: int = 14,
    price_col: str = "Close"
) -> pd.DataFrame:
    """
    Calculate the Relative Strength Index (RSI) for a given window period.

    Formula:
        Price Change = Close_t - Close_{t-1}
        Gain = max(Price Change, 0)
        Loss = max(-Price Change, 0)
        RS = Exponential/Simple Average Gain / Exponential/Simple Average Loss
        RSI = 100 - (100 / (1 + RS))

    Parameters:
        df (pd.DataFrame): Input stock DataFrame containing price column.
        period (int): Lookback period for RSI (default: 14).
        price_col (str): Column name to compute RSI on (default: 'Close').

    Returns:
        pd.DataFrame: DataFrame with added column `RSI_{period}`.
    """
    df = df.copy()
    rsi_col = f"RSI_{period}"

    delta = df[price_col].diff()

    # Separate positive gains and negative losses
    gain = np.where(delta > 0, delta, 0.0)
    loss = np.where(delta < 0, -delta, 0.0)

    # Convert to Series for rolling mean calculations
    gain_series = pd.Series(gain, index=df.index)
    loss_series = pd.Series(loss, index=df.index)

    # Use Exponential Moving Average (Wilder's Smoothing) for standard RSI computation
    avg_gain = gain_series.ewm(alpha=1/period, min_periods=period, adjust=False).mean()
    avg_loss = loss_series.ewm(alpha=1/period, min_periods=period, adjust=False).mean()

    # Calculate Relative Strength (RS) & RSI
    # Handle division by zero gracefully using np.where
    rs = np.where(avg_loss == 0, 100.0, avg_gain / avg_loss)
    rsi = 100.0 - (100.0 / (1.0 + rs))

    df[rsi_col] = np.round(rsi, 2)

    print(f"[Indicators] Added {rsi_col} technical indicator.")
    return df


def add_exponential_moving_averages(
    df: pd.DataFrame,
    short_window: int = 20,
    long_window: int = 50,
    price_col: str = "Close"
) -> pd.DataFrame:
    """
    Calculate short-term and long-term Exponential Moving Averages (EMA).

    Parameters:
        df (pd.DataFrame): Input stock DataFrame.
        short_window (int): Window period for short-term EMA (default: 20).
        long_window (int): Window period for long-term EMA (default: 50).
        price_col (str): Column name (default: 'Close').

    Returns:
        pd.DataFrame: DataFrame with added columns `EMA_{short_window}` and `EMA_{long_window}`.
    """
    df = df.copy()
    short_col = f"EMA_{short_window}"
    long_col = f"EMA_{long_window}"

    df[short_col] = df[price_col].ewm(span=short_window, adjust=False).mean()
    df[long_col] = df[price_col].ewm(span=long_window, adjust=False).mean()

    print(f"[Indicators] Added {short_col} and {long_col} indicators.")
    return df


def add_bollinger_bands(
    df: pd.DataFrame,
    window: int = 20,
    num_std: float = 2.0,
    price_col: str = "Close"
) -> pd.DataFrame:
    """
    Calculate Bollinger Bands (Middle, Upper, and Lower Bands).

    Parameters:
        df (pd.DataFrame): Input stock DataFrame.
        window (int): Moving average lookback window (default: 20).
        num_std (float): Standard deviations multiplier (default: 2.0).
        price_col (str): Price column to calculate bands from (default: 'Close').

    Returns:
        pd.DataFrame: DataFrame with added columns `BB_Middle`, `BB_Upper`, and `BB_Lower`.
    """
    df = df.copy()
    
    # Middle Band is standard SMA
    df['BB_Middle'] = df[price_col].rolling(window=window, min_periods=1).mean()
    
    # Rolling standard deviation
    rolling_std = df[price_col].rolling(window=window, min_periods=1).std().fillna(0)
    
    # Upper and Lower Bands
    df['BB_Upper'] = df['BB_Middle'] + (num_std * rolling_std)
    df['BB_Lower'] = df['BB_Middle'] - (num_std * rolling_std)

    print("[Indicators] Added Bollinger Bands (Middle, Upper, Lower).")
    return df


def add_macd(
    df: pd.DataFrame,
    fast_period: int = 12,
    slow_period: int = 26,
    signal_period: int = 9,
    price_col: str = "Close"
) -> pd.DataFrame:
    """
    Calculate Moving Average Convergence Divergence (MACD).

    Parameters:
        df (pd.DataFrame): Input stock DataFrame.
        fast_period (int): Fast EMA span (default: 12).
        slow_period (int): Slow EMA span (default: 26).
        signal_period (int): Signal EMA span (default: 9).
        price_col (str): Price column (default: 'Close').

    Returns:
        pd.DataFrame: DataFrame with added columns `MACD`, `MACD_Signal`, and `MACD_Hist`.
    """
    df = df.copy()
    
    fast_ema = df[price_col].ewm(span=fast_period, adjust=False).mean()
    slow_ema = df[price_col].ewm(span=slow_period, adjust=False).mean()
    
    df['MACD'] = fast_ema - slow_ema
    df['MACD_Signal'] = df['MACD'].ewm(span=signal_period, adjust=False).mean()
    df['MACD_Hist'] = df['MACD'] - df['MACD_Signal']

    print("[Indicators] Added MACD indicators (MACD, Signal, Histogram).")
    return df


def calculate_all_indicators(
    df: pd.DataFrame,
    short_ma: int = 20,
    long_ma: int = 50,
    rsi_period: int = 14
) -> pd.DataFrame:
    """
    Convenience wrapper to compute all technical indicators in sequence:
    SMA, EMA, Bollinger Bands, RSI, and MACD.

    Parameters:
        df (pd.DataFrame): Input stock DataFrame.
        short_ma (int): Short-term MA window (20).
        long_ma (int): Long-term MA window (50).
        rsi_period (int): RSI window (14).

    Returns:
        pd.DataFrame: DataFrame containing all computed technical indicators.
    """
    df_analyzed = add_moving_averages(df, short_window=short_ma, long_window=long_ma)
    df_analyzed = add_exponential_moving_averages(df_analyzed, short_window=short_ma, long_window=long_ma)
    df_analyzed = add_bollinger_bands(df_analyzed, window=short_ma)
    df_analyzed = add_rsi(df_analyzed, period=rsi_period)
    df_analyzed = add_macd(df_analyzed)
    return df_analyzed
