#!/usr/bin/env python3
"""Debug limit parameter."""
import sys
import os
import ccxt

exchange = ccxt.phemex({'enableRateLimit': True})
exchange.load_markets()

# Test different limits
test_limits = [10, 50, 100, 150, 200, 500, 1000]
for limit in test_limits:
    try:
        candles = exchange.fetch_ohlcv('BTC/USDT:USDT', '1h', limit=limit)
        print(f"Limit {limit}: SUCCESS - {len(candles)} candles", file=sys.stderr)
    except Exception as e:
        print(f"Limit {limit}: ERROR - {str(e)[:100]}", file=sys.stderr)
