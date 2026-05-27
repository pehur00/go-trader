#!/usr/bin/env python3
"""Debug with full exception tracing."""
import sys
import os
import traceback

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'platforms', 'phemex'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'shared_tools'))

from adapter import PhemexExchangeAdapter

adapter = PhemexExchangeAdapter()
print("Markets loaded before call:", adapter._markets_loaded, file=sys.stderr)

try:
    print("Calling get_perp_ohlcv...", file=sys.stderr)
    candles = adapter.get_perp_ohlcv('BTC', interval='1h', limit=200)
    print(f"Result: {len(candles)} candles", file=sys.stderr)
except Exception as e:
    print(f"Exception: {e}", file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
