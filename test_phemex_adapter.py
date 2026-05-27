#!/usr/bin/env python3
"""Test Phemex adapter - fetch OHLCV data in paper mode."""
import sys
sys.path.insert(0, 'platforms/phemex')
from adapter import PhemexExchangeAdapter

adapter = PhemexExchangeAdapter()
print(f"Adapter loaded OK, mode: {adapter.mode}")
print(f"Is live: {adapter.is_live}")

candles = adapter.get_perp_ohlcv('BTC', '1h', 10)
print(f"OHLCV candles fetched: {len(candles)}")
if candles:
    print(f"Latest candle: {candles[-1]}")

price = adapter.get_perp_price('BTC')
print(f"BTC perp price: {price}")

funding = adapter.get_funding_rate('BTC')
print(f"BTC funding rate: {funding}")
