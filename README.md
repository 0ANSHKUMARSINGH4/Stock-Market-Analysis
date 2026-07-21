# 📈 Stock Market Analysis using Python

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Scientific%20Computing-013243.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c.svg)](https://matplotlib.org/)
[![yfinance](https://img.shields.io/badge/yfinance-Market%20Data-00c853.svg)](https://pypi.org/project/yfinance/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A modular, intermediate-level Python application designed to download historical stock market data, process price trends using **Pandas** and **NumPy**, calculate core technical indicators (**SMA, EMA, Bollinger Bands, RSI, and MACD**), and generate professional multi-pane financial charts with **Matplotlib**.

> **Resume Impact Highlight**:
> *"Developed a Python application to analyze historical stock market data and visualize price trends. Processed and analyzed stock data using Pandas and NumPy, calculated technical indicators such as Moving Averages and RSI, and generated visual reports using Matplotlib."*

---

## 🌟 Key Features

- **Automated Data Ingestion**: Downloads historical daily stock quotes (OHLCV) directly via Yahoo Finance (`yfinance`).
- **Interactive CLI & CLI Arguments**: Accept tickers (e.g. `AAPL`, `MSFT`, `TSLA`, `NVDA`) and custom periods either dynamically or via script parameters.
- **Advanced Technical Indicators**:
  - **Moving Averages**: 20-day/50-day Simple Moving Averages (**SMA**) and Exponential Moving Averages (**EMA**).
  - **Bollinger Bands**: 20-day volatility channel with Upper, Middle, and Lower bands (set at $\pm 2$ standard deviations).
  - **RSI (14)**: Relative Strength Index oscillator measuring momentum and overbought/oversold levels.
  - **MACD (12, 26, 9)**: Moving Average Convergence Divergence line, signal line, and daily histogram bars.
- **4-Pane Visual Report**:
  - **Panel 1**: Price trend lines (Close, SMAs, EMA) with a semi-transparent Bollinger Bands volatility channel.
  - **Panel 2**: Daily transaction Volume bars (green for positive price change, red for negative).
  - **Panel 3**: MACD Convergence/Divergence lines and histogram difference bars.
  - **Panel 4**: RSI oscillator line with overbought ($\ge 70$) and oversold ($\le 30$) highlighted bands.
- **Data Export & Auto-Saving**: Automatically writes raw downloads to `data/`, analyzed outputs to `output/{TICKER}_analyzed.csv`, and dashboards to `images/{TICKER}_chart.png`.

---

## 📂 Project Structure

```text
Stock Market Analysis using Python/
├── data/                  # Raw downloaded historical stock data (CSV)
│   ├── AAPL_raw.csv
│   └── .gitkeep
├── output/                # Processed stock data with technical indicators (CSV)
│   ├── AAPL_analyzed.csv
│   └── .gitkeep
├── images/                # Generated financial dashboard chart figures (PNG)
│   ├── AAPL_chart.png
│   └── .gitkeep
├── src/                   # Source modules
│   ├── __init__.py        # Package initialization
│   ├── downloader.py      # Stock historical data retriever
│   ├── indicators.py      # Vectorized technical indicator computations
│   ├── visualization.py   # 4-pane Matplotlib dashboard generator
│   └── main.py            # CLI pipeline orchestrator
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
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
git clone https://github.com/0ANSHKUMARSINGH4/Stock-Market-Analysis.git
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
Run the main script without parameters to trigger interactive inputs:
```bash
python src/main.py
```
**Example Console Session**:
```text
============================================================
        STOCK MARKET ANALYSIS USING PYTHON        
============================================================

[Input Required]
Enter Stock Ticker Symbol (e.g. AAPL, MSFT, TSLA) [Default: AAPL]: AAPL

[Pipeline Initialization] Analyzing Ticker: 'AAPL' for Period: '1y'
------------------------------------------------------------
[Downloader] Fetching data for ticker: 'AAPL'...
[Downloader] Successfully fetched 252 rows of data for 'AAPL'.
[Downloader] Saved raw data to: data\AAPL_raw.csv

[Analysis Phase] Calculating Technical Indicators...
[Indicators] Added SMA_20 and SMA_50 indicators.
[Indicators] Added EMA_20 and EMA_50 indicators.
[Indicators] Added Bollinger Bands (Middle, Upper, Lower).
[Indicators] Added RSI_14 technical indicator.
[Indicators] Added MACD indicators (MACD, Signal, Histogram).

[Export Success] Analyzed dataset exported to CSV: output\AAPL_analyzed.csv

[Dataset Summary]
      Date      Close     SMA_20     EMA_20   BB_Upper   BB_Lower     MACD  RSI_14
2026-07-15 327.500000 301.927499 306.784438 329.825669 274.029330 6.611093   68.78
2026-07-16 333.260010 303.628500 309.305921 334.793926 272.463075 7.879707   71.44
2026-07-17 333.739990 305.517999 311.632975 339.203655 271.832343 8.822128   71.66
2026-07-20 326.589996 306.946999 313.057453 341.699521 272.194476 8.889585   63.88
2026-07-21 327.769989 308.484998 314.458647 344.097825 272.872170 8.935260   64.56

[Visualization Phase] Generating and auto-saving chart dashboard...
[Visualization] Generating comprehensive 4-panel chart dashboard for 'AAPL'...
[Visualization] Stock chart auto-saved to: images\AAPL_chart.png
```

### Option 2: Command Line Argument Mode
Pass custom tickers, periods, or suppress visualization popups:
```bash
# Analyze Microsoft stock over a 6-month period
python src/main.py --ticker MSFT --period 6m

# Run batch script mode without GUI popups
python src/main.py --ticker NVDA --period 2y --no-show
```

---

## 📊 Technical Indicators Explained

| Indicator | Formula / Method | Interpretation |
| :--- | :--- | :--- |
| **Simple Moving Average (SMA)** | $\text{SMA}_n = \frac{1}{n} \sum_{i=0}^{n-1} P_{t-i}$ | Highlights overall trend direction and standard support/resistance areas. |
| **Exponential Moving Average (EMA)** | $\text{EMA}_t = \left(P_t \cdot \frac{2}{n+1}\right) + \text{EMA}_{t-1} \cdot \left(1 - \frac{2}{n+1}\right)$ | Places greater weight on recent prices to reduce lag compared to SMAs. |
| **Bollinger Bands (BB)** | $\text{Upper/Lower} = \text{SMA}_{20} \pm (2 \times \sigma_{20})$ | Shaded channel indicating price volatility. Touching upper bands implies overbought status. |
| **Relative Strength Index (RSI)** | $\text{RSI} = 100 - \left(\frac{100}{1 + \text{RS}}\right)$ | Oscillator ranging from 0-100. Readings $\ge 70$ indicate overbought levels; readings $\le 30$ indicate oversold levels. |
| **MACD** | $\text{MACD} = \text{EMA}_{12} - \text{EMA}_{26}$ | Momentum indicator showing relationship between two EMAs. Divergences signal price reversals. |

---

## 🖼️ Sample Visualizations

Generated financial dashboard charts are saved to the `images/` directory:

| Ticker | Output Chart Preview |
| :---: | :--- |
| **AAPL** | `images/AAPL_chart.png` *(Price, SMAs, EMA, Bollinger Bands, Volume, MACD, RSI 14)* |
| **MSFT** | `images/MSFT_chart.png` *(Price, SMAs, EMA, Bollinger Bands, Volume, MACD, RSI 14)* |

---

## 🛠️ Tech Stack & Libraries

- **Language**: Python 3.9+
- **Data Ingestion**: `yfinance`
- **Data Manipulation**: `pandas`, `numpy`
- **Data Visualization**: `matplotlib`

---

## 🔮 Future Enhancements

- [ ] Support multi-ticker comparison dashboard on a single figure.
- [ ] Implement interactive web GUI using **Streamlit** or **Dash**.
- [ ] Incorporate automated sentiment analysis on stock news.
- [ ] Incorporate simple buy/sell backtesting signals based on indicator crossovers.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more details.
