#!/usr/bin/env python3
"""Debug check_phemex paths."""
import sys
import os

print("Script __file__:", __file__, file=sys.stderr)
print("Script dirname:", os.path.dirname(__file__), file=sys.stderr)
print("CWD:", os.getcwd(), file=sys.stderr)

phemex_path = os.path.join(os.path.dirname(__file__), '..', 'platforms', 'phemex')
print("Phemex path (relative):", phemex_path, file=sys.stderr)
print("Phemex path (abs):", os.path.abspath(phemex_path), file=sys.stderr)
print("Phemex path exists:", os.path.exists(phemex_path), file=sys.stderr)

sys.path.insert(0, phemex_path)
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'shared_tools'))

print("sys.path[0]:", sys.path[0], file=sys.stderr)

from adapter import PhemexExchangeAdapter
adapter = PhemexExchangeAdapter()
print("Adapter created, mode:", adapter.mode, file=sys.stderr)

candles = adapter.get_perp_ohlcv('BTC', interval='1h', limit=10)
print("Candles count:", len(candles), file=sys.stderr)
