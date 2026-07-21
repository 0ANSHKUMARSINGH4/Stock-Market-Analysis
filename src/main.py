"""
main.py
-------
Main execution script for the "Stock Market Analysis using Python" application.
Provides interactive CLI input or command-line arguments to download historical stock data,
compute 20-day MA, 50-day MA, and RSI (14) technical indicators, export processed CSV results,
and automatically save visual financial chart dashboards.
"""

import sys
import os
import argparse
import pandas as pd

# Add src to system path to ensure package imports work seamlessly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from downloader import fetch_stock_data
from indicators import calculate_all_indicators
from visualization import plot_stock_analysis


def parse_arguments() -> argparse.Namespace:
    """
    Parse optional command line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Stock Market Analysis using Python - Download, Analyze, and Visualize Stock Price Data."
    )
    parser.add_argument(
        "-t", "--ticker",
        type=str,
        default=None,
        help="Stock ticker symbol (e.g. AAPL, MSFT, TSLA, GOOGL)"
    )
    parser.add_argument(
        "-p", "--period",
        type=str,
        default="1y",
        help="Historical period to download (e.g. 1m, 6m, 1y, 2y, 5y). Default: 1y"
    )
    parser.add_argument(
        "--no-show",
        action="store_true",
        help="Do not display plot window interactively (useful for automated batch scripts)"
    )
    return parser.parse_args()


def main():
    """
    Main application pipeline function.
    """
    print("=" * 60)
    print("        STOCK MARKET ANALYSIS USING PYTHON        ")
    print("=" * 60)

    args = parse_arguments()

    # Handle interactive user input if ticker argument was not passed
    ticker = args.ticker
    if not ticker:
        print("\n[Input Required]")
        user_input = input("Enter Stock Ticker Symbol (e.g. AAPL, MSFT, TSLA) [Default: AAPL]: ").strip()
        ticker = user_input.upper() if user_input else "AAPL"
    else:
        ticker = ticker.strip().upper()

    period = args.period.strip()

    print(f"\n[Pipeline Initialization] Analyzing Ticker: '{ticker}' for Period: '{period}'")
    print("-" * 60)

    # 1. Download Historical Stock Data
    try:
        raw_df = fetch_stock_data(
            ticker=ticker,
            period=period,
            save_raw=True,
            data_dir="data"
        )
    except Exception as err:
        print(f"\n[Error] Stopping pipeline due to data download error: {err}")
        sys.exit(1)

    # 2. Calculate Technical Indicators
    print("\n[Analysis Phase] Calculating Technical Indicators...")
    analyzed_df = calculate_all_indicators(
        df=raw_df,
        short_ma=20,
        long_ma=50,
        rsi_period=14
    )

    # 3. Export Processed Data to CSV
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_csv_path = os.path.join(output_dir, f"{ticker}_analyzed.csv")
    analyzed_df.to_csv(output_csv_path, index=False)
    print(f"\n[Export Success] Analyzed dataset exported to CSV: {output_csv_path}")

    # Display dataset preview snippet
    print("\n[Dataset Summary]")
    print(analyzed_df[['Date', 'Close', 'SMA_20', 'SMA_50', 'RSI_14']].tail(5).to_string(index=False))

    # 4. Generate & Save Stock Analysis Visualizations
    images_dir = "images"
    os.makedirs(images_dir, exist_ok=True)
    chart_save_path = os.path.join(images_dir, f"{ticker}_chart.png")

    print("\n[Visualization Phase] Generating and auto-saving chart dashboard...")
    plot_stock_analysis(
        df=analyzed_df,
        ticker=ticker,
        save_path=chart_save_path,
        show_plot=not args.no_show
    )

    print("\n" + "=" * 60)
    print(f" SUCCESS! Analysis complete for {ticker}.")
    print(f" Raw Data:   data/{ticker}_raw.csv")
    print(f" Processed:  output/{ticker}_analyzed.csv")
    print(f" Chart:      images/{ticker}_chart.png")
    print("=" * 60)


if __name__ == "__main__":
    main()
