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

print(data)

#[{'No.': '1', 'Ticker': '1', 'Company': '1', 'Sector': '1', 'Industry': '1', 'Country': '1', 'Market Cap': '1', 'P/E': '1', 'Price': '1', 'Change': '1', 'Volume': '1'}, {'No.': '1', 'Ticker': 'BTCM', 'Company': 'BIT Mining Limited', 'Sector': 'Technology', 'Industry': 'Information Technology Services', 'Country': 'Hong Kong', 'Market Cap': '36.69M', 'P/E': '-', 'Price': '4.09', 'Change': '0.00%', 'Volume': '1,122,310'}, {'No.': '1', 'Ticker': 'BIT Mining Limited', 'Company': 'Information Technology Services', 'Sector': '36.69M', 'Industry': '4.09', 'Country': '1,122,310', 'Market Cap': 'ICD', 'P/E': 'Energy', 'Price': 'USA', 'Change': '-', 'Volume': '1.37%'}, {'No.': '1', 'Ticker': 'Technology', 'Company': '36.69M', 'Sector': '0.00%', 'Industry': 'ICD', 'Country': 'Oil & Gas Drilling', 'Market Cap': '-', 'P/E': '201,295', 'Price': 'Party City Holdco Inc.', 'Change': 'USA', 'Volume': '0.37'}, {'No.': '1', 'Ticker': 'Information Technology Services', 'Company': '4.09', 'Sector': 'ICD', 'Industry': 'USA', 'Country': '1.37%', 'Market Cap': 'Party City Holdco Inc.', 'P/E': '42.40M', 'Price': '32,916,676', 'Change': 'Technology', 'Volume': '-'}]

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
- 


#### Technical


# TODO
- This readme