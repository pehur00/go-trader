#!/usr/bin/env python3
"""Debug Phemex symbol format."""
import sys
import os
import ccxt

exchange = ccxt.phemex({'enableRateLimit': True})
exchange.load_markets()

# List all perpetual swap symbols
perps = [s for s in exchange.symbols if ':USDT' in s]
print("Perpetual USDT symbols (first 20):", perps[:20], file=sys.stderr)

# Check BTC specifically
btc_perps = [s for s in perps if 'BTC' in s]
print("BTC perps:", btc_perps, file=sys.stderr)

# Try different symbol formats
test_symbols = [
    'BTC/USDT:USDT',
    'BTC/USDT:USDT:USDT',
    'BTC:USDT',
    'BTCUSDT',
]

for sym in test_symbols:
    try:
        candles = exchange.fetch_ohlcv(sym, '1h', limit=5)
        print(f"{sym}: SUCCESS - {len(candles)} candles", file=sys.stderr)
    except Exception as e:
        print(f"{sym}: ERROR - {e}", file=sys.stderr)
