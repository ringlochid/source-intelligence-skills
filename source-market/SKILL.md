---
name: source-market
description: Gather finance, stock, BTC, crypto, company, and market sources. Use finance/Finnhub-style data plus independent price/data verification; route to source-briefing with risk labels.
---

# Source Market

Use for finance, BTC, crypto, companies, tickers, and market-moving sources.

## Source pattern

Use finance-data/Finnhub-style sources plus built-in finance price checks where available. For primary facts, prefer company IR, filings, exchange/regulator statements, official project posts, and reputable finance wires.


## Reference links

Use market/news sources as context, but verify price/data separately:

- Finnhub API docs: https://finnhub.io/docs/api
- SEC EDGAR search: https://www.sec.gov/edgar/search/
- Yahoo Finance: https://finance.yahoo.com/
- CoinGecko API docs: https://docs.coingecko.com/reference/introduction
- CoinMarketCap API docs: https://coinmarketcap.com/api/documentation/v1/

## Workflow

1. Identify ticker/coin/entity and time window.
2. Verify current price/market data separately from commentary.
3. Collect filings/statements/news/context.
4. Separate market data, reported news, and analyst/social interpretation.
5. Send source notes to `source-briefing`.

Do not present investment advice. Use confidence/risk labels and concrete timestamps.
