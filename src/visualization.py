"""
visualization.py
----------------
Module responsible for generating interactive multi-pane financial charts using Matplotlib.
Renders Price Trends + Moving Averages, Trading Volume, and RSI (14) indicators.
"""

import os
from typing import Optional
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator


def plot_stock_analysis(
    df: pd.DataFrame,
    ticker: str,
    save_path: Optional[str] = None,
    show_plot: bool = False
) -> None:
    """
    Generate a 3-panel visual report for stock market analysis.

    Panel 1: Closing Price, 20-Day Simple Moving Average, 50-Day Simple Moving Average.
    Panel 2: Daily Trading Volume (colored by price movement: green = gain, red = loss).
    Panel 3: Relative Strength Index (RSI 14) with 70 (Overbought) & 30 (Oversold) lines.

    Parameters:
        df (pd.DataFrame): DataFrame containing stock data & calculated indicators.
        ticker (str): Stock ticker symbol.
        save_path (str, optional): Filepath to auto-save figure PNG.
        show_plot (bool): Whether to call plt.show() interactively.
    """
    ticker_clean = ticker.upper()
    print(f"[Visualization] Generating chart dashboard for '{ticker_clean}'...")

    # Ensure Date column is datetime type
    dates = pd.to_datetime(df['Date'])

    # Determine up/down days for volume bar coloring
    price_diff = df['Close'].diff().fillna(0)
    vol_colors = ['#26a69a' if diff >= 0 else '#ef5350' for diff in price_diff]

    # Setup dark modern financial aesthetic
    plt.style.use('dark_background')
    fig, (ax_price, ax_vol, ax_rsi) = plt.subplots(
        nrows=3,
        ncols=1,
        figsize=(14, 10),
        sharex=True,
        gridspec_kw={'height_ratios': [3, 1, 1.2]}
    )

    fig.patch.set_facecolor('#121212')

    # ==========================================
    # Panel 1: Closing Price & Moving Averages
    # ==========================================
    ax_price.set_facecolor('#1e1e1e')
    ax_price.plot(dates, df['Close'], label='Close Price', color='#ffffff', linewidth=1.8, alpha=0.95)

    if 'SMA_20' in df.columns:
        ax_price.plot(dates, df['SMA_20'], label='20-Day SMA', color='#29b6f6', linewidth=1.4, linestyle='--')
    if 'SMA_50' in df.columns:
        ax_price.plot(dates, df['SMA_50'], label='50-Day SMA', color='#ffa726', linewidth=1.4, linestyle='--')

    ax_price.set_title(f"{ticker_clean} - Stock Price Analysis & Technical Indicators", fontsize=16, fontweight='bold', pad=12, color='#ffffff')
    ax_price.set_ylabel("Price ($)", fontsize=11, color='#e0e0e0')
    ax_price.legend(loc='upper left', frameon=True, facecolor='#2a2a2a', edgecolor='none', labelcolor='#ffffff')
    ax_price.grid(True, linestyle=':', alpha=0.3, color='#666666')

    # ==========================================
    # Panel 2: Daily Trading Volume
    # ==========================================
    ax_vol.set_facecolor('#1e1e1e')
    ax_vol.bar(dates, df['Volume'] / 1e6, color=vol_colors, alpha=0.75, width=0.8, label='Volume (Millions)')
    ax_vol.set_ylabel("Volume (M)", fontsize=11, color='#e0e0e0')
    ax_vol.legend(loc='upper left', frameon=True, facecolor='#2a2a2a', edgecolor='none', labelcolor='#ffffff')
    ax_vol.grid(True, linestyle=':', alpha=0.3, color='#666666')

    # ==========================================
    # Panel 3: Relative Strength Index (RSI 14)
    # ==========================================
    ax_rsi.set_facecolor('#1e1e1e')
    rsi_col = [col for col in df.columns if col.startswith('RSI')][0] if any(col.startswith('RSI') for col in df.columns) else 'RSI_14'
    
    if rsi_col in df.columns:
        ax_rsi.plot(dates, df[rsi_col], label=f'{rsi_col}', color='#ab47bc', linewidth=1.5)
        # Reference threshold lines
        ax_rsi.axhline(70, color='#ef5350', linestyle='--', linewidth=1, label='Overbought (70)')
        ax_rsi.axhline(30, color='#66bb6a', linestyle='--', linewidth=1, label='Oversold (30)')
        # Fill overbought/oversold regions
        ax_rsi.fill_between(dates, df[rsi_col], 70, where=(df[rsi_col] >= 70), color='#ef5350', alpha=0.25)
        ax_rsi.fill_between(dates, df[rsi_col], 30, where=(df[rsi_col] <= 30), color='#66bb6a', alpha=0.25)

    ax_rsi.set_ylim(0, 100)
    ax_rsi.set_ylabel("RSI", fontsize=11, color='#e0e0e0')
    ax_rsi.set_xlabel("Date", fontsize=11, color='#e0e0e0')
    ax_rsi.legend(loc='upper left', frameon=True, facecolor='#2a2a2a', edgecolor='none', labelcolor='#ffffff', fontsize=9)
    ax_rsi.grid(True, linestyle=':', alpha=0.3, color='#666666')

    # Format Date Axis
    ax_rsi.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    ax_rsi.xaxis.set_major_locator(MaxNLocator(10))
    fig.autofmt_xdate()

    plt.tight_layout()

    # Save figure if path provided
    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor=fig.get_facecolor())
        print(f"[Visualization] Stock chart auto-saved to: {save_path}")

    if show_plot:
        plt.show()
    
    plt.close(fig)
