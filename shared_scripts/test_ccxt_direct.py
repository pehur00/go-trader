#!/usr/bin/env python3
"""Debug with verbose output."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'platforms', 'phemex'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'shared_tools'))

import ccxt

exchange = ccxt.phemex({'enableRateLimit': True})
print("Loading markets...", file=sys.stderr)
exchange.load_markets()
print("Markets loaded. BTC/USDT:USDT in symbols:", 'BTC/USDT:USDT' in exchange.symbols, file=sys.stderr)

print("Fetching OHLCV...", file=sys.stderr)
try:
    candles = exchange.fetch_ohlcv('BTC/USDT:USDT', '1h', limit=200)
    print(f"SUCCESS: {len(candles)} candles", file=sys.stderr)
    if candles:
        print(f"Last candle: {candles[-1]}", file=sys.stderr)
except Exception as e:
    print(f"ERROR: {e}", file=sys.stderr)
    import traceback
    traceback.print_exc(file=sys.stderr)
