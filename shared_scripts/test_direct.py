#!/usr/bin/env python3
"""Direct test of check_phemex flow."""
import sys
import os
import json
import math

# Exact same path setup as check_phemex.py
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'platforms', 'phemex'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'shared_strategies', 'open', 'futures'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'shared_tools'))

from adapter import PhemexExchangeAdapter

adapter = PhemexExchangeAdapter()
print("Adapter mode:", adapter.mode, file=sys.stderr)

# Direct call like check_phemex does
candles = adapter.get_perp_ohlcv('BTC', interval='1h', limit=200)
print(f"get_perp_ohlcv returned {len(candles)} candles", file=sys.stderr)

if candles:
    print(f"First: {candles[0]}", file=sys.stderr)
    print(f"Last: {candles[-1]}", file=sys.stderr)
else:
    print("No candles - testing direct ccxt call", file=sys.stderr)
    try:
        direct = adapter._exchange.fetch_ohlcv('BTC/USDT:USDT', '1h', limit=200)
        print(f"Direct ccxt returned {len(direct)} candles", file=sys.stderr)
    except Exception as e:
        print(f"Direct ccxt error: {e}", file=sys.stderr)
