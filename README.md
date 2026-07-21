# 📈 Stock Market Analysis using Python

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)
[![yfinance](https://img.shields.io/badge/yfinance-Market%20Data-00c853.svg)](https://pypi.org/project/yfinance/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A modular, beginner-to-intermediate Python application designed to download historical stock market data, process price trends using **Pandas** and **NumPy**, calculate technical indicators (**20-Day & 50-Day Simple Moving Averages**, **14-Day RSI**), and generate multi-pane financial charts with **Matplotlib**.

> **Resume Impact Highlight**:
> *"Developed a Python application to analyze historical stock market data and visualize price trends. Processed and analyzed stock data using Pandas and NumPy, calculated technical indicators such as Moving Averages and RSI, and generated visual reports using Matplotlib."*

---

## 🌟 Key Features

- **Automated Data Retrieval**: Downloads historical OHLCV (Open, High, Low, Close, Volume) market data directly via Yahoo Finance (`yfinance`).
- **Interactive Ticker Selection**: Accepts user-defined ticker symbols (e.g. `AAPL`, `MSFT`, `TSLA`, `NVDA`, `GOOGL`) or command-line parameters.
- **Technical Indicator Computation**:
  - **20-Day Simple Moving Average (SMA_20)**: Short-term price trend indicator.
  - **50-Day Simple Moving Average (SMA_50)**: Medium-to-long term price trend indicator.
  - **14-Day Relative Strength Index (RSI_14)**: Momentum oscillator measuring overbought (>=70) and oversold (<=30) conditions.
- **Multi-Pane Dashboard Visualization**:
  - **Top Panel**: Price trend line with overlaid 20-day & 50-day moving averages.
  - **Middle Panel**: Daily trading volume bar chart (color-coded green for gain days, red for loss days).
  - **Bottom Panel**: RSI indicator with shaded overbought and oversold boundary zones.
- **Data Export & Auto-Saving**: Automatically saves clean raw data to `data/`, analyzed indicator data to `output/{TICKER}_analyzed.csv`, and figure dashboards to `images/{TICKER}_chart.png`.

---

## 📂 Project Structure

```text
Stock Market Analysis using Python/
├── data/                  # Storage for raw downloaded historical stock data (CSV)
│   ├── AAPL_raw.csv
│   └── .gitkeep
├── output/                # Storage for processed data with technical indicators (CSV)
│   ├── AAPL_analyzed.csv
│   └── .gitkeep
├── images/                # Auto-saved multi-panel financial chart figures (PNG)
│   ├── AAPL_chart.png
│   └── .gitkeep
├── src/                   # Source code modules
│   ├── __init__.py        # Package initialization
│   ├── downloader.py      # Stock historical data fetcher module
│   ├── indicators.py      # Vectorized technical indicator computations
│   ├── visualization.py   # Multi-pane Matplotlib dashboard generator
│   └── main.py            # Main entry point and CLI pipeline orchestrator
├── README.md              # Project documentation
├── requirements.txt       # Project dependencies
└── .gitignore             # Version control exclusions
```

---

## ⚙️ Installation & Setup

### 1. Prerequisites
Ensure Python 3.9+ is installed on your system. Verify with:
```bash
python --version
```

### 2. Clone the Repository
```bash
git clone https://github.com/your-username/Stock-Market-Analysis.git
cd Stock-Market-Analysis
```

### 3. Set Up Virtual Environment (Recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage Guide

### Option 1: Interactive Prompt Mode
Run the main script without parameters to trigger interactive user inputs:
```bash
python src/main.py
```
**Example Console Session**:
```text
============================================================
        STOCK MARKET ANALYSIS USING PYTHON        
============================================================

[Input Required]
Enter Stock Ticker Symbol (e.g. AAPL, MSFT, TSLA) [Default: AAPL]: TSLA

[Pipeline Initialization] Analyzing Ticker: 'TSLA' for Period: '1y'
------------------------------------------------------------
[Downloader] Fetching data for ticker: 'TSLA'...
[Downloader] Successfully fetched 252 rows of data for 'TSLA'.
[Downloader] Saved raw data to: data\TSLA_raw.csv

[Analysis Phase] Calculating Technical Indicators...
[Indicators] Added SMA_20 and SMA_50 indicators.
[Indicators] Added RSI_14 technical indicator.

[Export Success] Analyzed dataset exported to CSV: output\TSLA_analyzed.csv

[Visualization Phase] Generating and auto-saving chart dashboard...
[Visualization] Generating chart dashboard for 'TSLA'...
[Visualization] Stock chart auto-saved to: images\TSLA_chart.png
```

### Option 2: Command Line Argument Mode
Pass custom tickers, lookback periods, or suppress plot popup display:
```bash
# Analyze Microsoft stock over a 6-month period
python src/main.py --ticker MSFT --period 6m

# Run automated analysis without popping up GUI plot window
python src/main.py --ticker NVDA --period 1y --no-show
```

---

## 📊 Technical Indicators Explained

| Indicator | Formula / Method | Interpretation |
| :--- | :--- | :--- |
| **Simple Moving Average (SMA)** | $\text{SMA}_n = \frac{1}{n} \sum_{i=0}^{n-1} P_{t-i}$ | Identifies overall trend direction and key support/resistance levels. A bullish "Golden Cross" occurs when SMA-20 crosses above SMA-50. |
| **Relative Strength Index (RSI)** | $\text{RSI} = 100 - \left(\frac{100}{1 + \text{RS}}\right)$ | Measures speed and change of price movements. Values $\ge 70$ signal overbought conditions (potential pullback); values $\le 30$ signal oversold conditions. |

---

## 🖼️ Sample Visualizations

Generated financial dashboard charts are saved to the `images/` directory:

| Ticker | Output Chart Preview |
| :---: | :--- |
| **AAPL** | `images/AAPL_chart.png` *(Price, 20-Day SMA, 50-Day SMA, Trading Volume, RSI 14)* |
| **MSFT** | `images/MSFT_chart.png` *(Price, 20-Day SMA, 50-Day SMA, Trading Volume, RSI 14)* |

---

## 🛠️ Tech Stack & Libraries

- **Language**: Python 3.9+
- **Data Ingestion**: `yfinance`
- **Data Manipulation**: `pandas`, `numpy`
- **Data Visualization**: `matplotlib`

---

## 🔮 Future Enhancements

- [ ] Add **Exponential Moving Averages (EMA)** and **MACD (Moving Average Convergence Divergence)**.
- [ ] Add **Bollinger Bands** volatility indicators.
- [ ] Support multi-ticker comparison dashboard on a single figure.
- [ ] Implement interactive web GUI using **Streamlit** or **Dash**.
- [ ] Incorporate automated sentiment analysis on stock news.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more details.
