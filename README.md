# FINVIZ Scraper

## How to use

```python 
from finscraper import Screener

filters = {
    "descriptive": {
        "exchange": "NYSE",
        "industry": "stocksonly"
    },
    "technical": {
        "performance": "1w30o"
    },
}

screener = Screener()

data = screener.query(filters=filters)

for row in data:
    print(row)

"""
{'No.': '1', 'Ticker': 'BTCM', 'Company': 'BIT Mining Limited', 'Sector': 'Technology', 'Industry': 'Information Technology Services', 'Country': 'Hong Kong', 'Market Cap': '36.69M', 'P/E': '-', 'Price': '4.09', 'Change': '0.00%', 'Volume': '1,122,310'}
{'No.': '2', 'Ticker': 'ICD', 'Company': 'Independence Contract Drilling, Inc.', 'Sector': 'Energy', 'Industry': 'Oil & Gas Drilling', 'Country': 'USA', 'Market Cap': '69.62M', 'P/E': '-', 'Price': '5.18', 'Change': '1.37%', 'Volume': '201,295'}
{'No.': '3', 'Ticker': 'PRTY', 'Company': 'Party City Holdco Inc.', 'Sector': 'Consumer Cyclical', 'Industry': 'Specialty Retail', 'Country': 'USA', 'Market Cap': '42.40M', 'P/E': '0.28', 'Price': '0.37', 'Change': '7.19%', 'Volume': '32,916,676'}
{'No.': '4', 'Ticker': 'SOS', 'Company': 'SOS Limited', 'Sector': 'Technology', 'Industry': 'Software - Infrastructure', 'Country': 'China', 'Market Cap': '43.47M', 'P/E': '-', 'Price': '7.33', 'Change': '6.39%', 'Volume': '384,651'}
{'No.': '5', 'Ticker': 'VLTA', 'Company': 'Volta Inc.', 'Sector': 'Consumer Cyclical', 'Industry': 'Specialty Retail', 'Country': 'USA', 'Market Cap': '149.27M', 'P/E': '-', 'Price': '0.88', 'Change': '2.26%', 'Volume': '5,774,167'}
"""

```
### Filters on the Finviz ui

The filters are split into **Descriptive**, **Fundamental** &  **Technical**

#### Descriptive filters
- Exchange
- Market Cap
- Earnings Rate
- Target Price
- Index
- Dividend Yield
- Average Volume
- IPO Date
- Sector
- Float Short
- Relative Volume
- Shares Outstanding
- Industry
- Analyst Recommendation
- Current Volume
- Float
- Country
- Option/Short
- Price


#### Fundamental
- P/E
- Price/Cash
- EPS growth next 5 years
- Return on Equity
- Debt/Equity
- Insider Ownership
- Forward P/E	
- Price/Free Cash Fl
- Sales growth past 5 years
- Return on Investment
- Gross Margin
- Insider Transactions
- PEG
- EPS growth this year
- EPS growth qtr over qtr
- Current Ratio
- Operating Margin
- Institutional Ownership
- P/S
- EPS growth next year
- Sales growth qtr over qtr
- Quick Ratio
- Net Profit Margin
- Institutional Transactions
- P/B
- EPS growth past 5 years
- Return on Assets
- LT Debt/Equity
- Payout Ratio


#### Technical
- Performance
- 20-Day Simple Moving Average
- 20-Day High/Low
- Beta
- Performance 2
- 50-Day Simple Moving Average
- 50-Day High/Low
- Average True Range
- Volatility
- 200-Day Simple Moving Average
- 52-Week High/Low
- RSI
- Change
- Pattern
- Gap
- Change from Ope
- Candlestick

# TODO
- Proxy to rotate IP's 