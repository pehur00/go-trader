#!/usr/bin/env python3
"""Debug script for Phemex adapter - run from shared_scripts dir."""
import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(script_dir, '..', 'platforms', 'phemex'))
sys.path.insert(0, os.path.join(script_dir, '..', 'shared_tools'))

from adapter import PhemexExchangeAdapter

adapter = PhemexExchangeAdapter()
print('Mode:', adapter.mode, file=sys.stderr)
print('Is live:', adapter.is_live, file=sys.stderr)

# Try fetching OHLCV directly
candles = adapter.get_perp_ohlcv('BTC', interval='1h', limit=10)
print('Candles count:', len(candles), file=sys.stderr)
if candles:
    print('First candle:', candles[0], file=sys.stderr)
    print('Last candle:', candles[-1], file=sys.stderr)
else:
    print('No candles returned', file=sys.stderr)
