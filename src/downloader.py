"""
downloader.py
----------------
Module responsible for downloading historical stock market data using the yfinance library.
Includes data validation, clean column formatting, and error handling.
"""

import os
from typing import Optional
import pandas as pd
import yfinance as yf


def fetch_stock_data(
    ticker: str,
    period: str = "1y",
    interval: str = "1d",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    save_raw: bool = True,
    data_dir: str = "data"
) -> pd.DataFrame:
    """
    Fetch historical stock data for a given ticker from Yahoo Finance.

    Parameters:
        ticker (str): The stock ticker symbol (e.g., 'AAPL', 'MSFT', 'TSLA').
        period (str): Valid period string if start_date/end_date not given (e.g., '1y', '6m', '2y').
        interval (str): Data interval (e.g., '1d', '1wk', '1mo').
        start_date (str, optional): Start date string (YYYY-MM-DD).
        end_date (str, optional): End date string (YYYY-MM-DD).
        save_raw (bool): Whether to save raw fetched data to CSV in `data_dir`.
        data_dir (str): Relative directory to store raw CSV data.

    Returns:
        pd.DataFrame: Formatted stock data containing columns:
                      ['Date', 'Open', 'High', 'Low', 'Close', 'Volume'].
    
    Raises:
        ValueError: If ticker is invalid or no data is returned.
    """
    ticker_clean = ticker.strip().upper()
    print(f"[Downloader] Fetching data for ticker: '{ticker_clean}'...")

    try:
        stock = yf.Ticker(ticker_clean)
        
        if start_date and end_date:
            df = stock.history(start=start_date, end=end_date, interval=interval)
        else:
            df = stock.history(period=period, interval=interval)

        if df.empty:
            raise ValueError(f"No data returned for ticker '{ticker_clean}'. Please check the symbol.")

        # Flatten multi-level columns if present (e.g., in newer yfinance versions)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        # Ensure 'Date' is a column, not just index
        df = df.reset_index()

        # Clean Date formatting to YYYY-MM-DD string or datetime
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date']).dt.tz_localize(None)

        # Standardize required columns
        required_cols = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        missing_cols = [col for col in required_cols if col not in df.columns]
        
        if missing_cols:
            raise ValueError(f"Fetched dataset is missing expected columns: {missing_cols}")

        df = df[required_cols].copy()
        df.sort_values(by='Date', ascending=True, inplace=True)
        df.reset_index(drop=True, inplace=True)

        print(f"[Downloader] Successfully fetched {len(df)} rows of data for '{ticker_clean}'.")

        # Save raw data if requested
        if save_raw:
            os.makedirs(data_dir, exist_ok=True)
            raw_path = os.path.join(data_dir, f"{ticker_clean}_raw.csv")
            df.to_csv(raw_path, index=False)
            print(f"[Downloader] Saved raw data to: {raw_path}")

        return df

    except Exception as e:
        print(f"[Downloader Error] Failed to download data for ticker '{ticker_clean}': {e}")
        raise
