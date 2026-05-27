#!/usr/bin/env python3
"""Debug Phemex timeframe formats."""
import sys
import os
import ccxt

exchange = ccxt.phemex({'enableRateLimit': True})
exchange.load_markets()

# Check what timeframes Phemex supports
print("Timeframes:", exchange.timeframes, file=sys.stderr)

# Try different resolutions
test_tf = ['1h', '1H', '60', '3600', 'H']
for tf in test_tf:
    try:
        candles = exchange.fetch_ohlcv('BTC/USDT:USDT', tf, limit=10)
        print(f"Timeframe {tf}: SUCCESS - {len(candles)} candles", file=sys.stderr)
    except Exception as e:
        print(f"Timeframe {tf}: ERROR - {str(e)[:100]}", file=sys.stderr)

# Try with no limit
try:
    candles = exchange.fetch_ohlcv('BTC/USDT:USDT', '1h')
    print(f"No limit: SUCCESS - {len(candles)} candles", file=sys.stderr)
except Exception as e:
    print(f"No limit: ERROR - {str(e)[:100]}", file=sys.stderr)

# Try with limit=100
try:
    candles = exchange.fetch_ohlcv('BTC/USDT:USDT', '1h', limit=100)
    print(f"Limit 100: SUCCESS - {len(candles)} candles", file=sys.stderr)
except Exception as e:
    print(f"Limit 100: ERROR - {str(e)[:100]}", file=sys.stderr)
