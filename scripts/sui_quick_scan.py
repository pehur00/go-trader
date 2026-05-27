#!/usr/bin/env python3
"""Quick SUI backtest scan across timeframes."""
import sys, os
os.chdir('/home/hermes/projects/go-trader')
sys.path.insert(0, 'backtest')
sys.path.insert(0, 'shared_tools')
sys.path.insert(0, 'shared_strategies/open')
sys.path.insert(0, 'platforms/phemex')

from backtest.run_backtest import run_single_backtest

strategies = ['squeeze_momentum', 'atr_breakout', 'momentum', 'supertrend', 'macd']
timeframes = ['30m', '15m', '5m']

capital = 1000
since = '2025-01-01'

print("="*70)
print("  SUI/USDT QUICK SCAN — 2025-01-01 → 2026-05-10")
print("="*70)

for tf in timeframes:
    print(f"\n{'='*70}")
    print(f"  TIMEFRAME: {tf}")
    print(f"{'='*70}")
    for strat in strategies:
        try:
            result = run_single_backtest(
                strategy_name=strat,
                symbol='SUI/USDT',
                timeframe=tf,
                since=since,
                capital=capital,
                registry='futures',
                platform='binanceus',
                htf_filter=False,
                close_strategies=None,
                regime_enabled=False,
            )
            if result:
                print(f"\n  {strat:20s} | Equity: ${result.get('final_equity',0):>8.2f} | Return: {result.get('total_return_pct',0):>+7.2f}% | Trades: {result.get('total_trades',0):>4} | Win%: {result.get('win_rate',0):>5.1f}% | MaxDD: {result.get('max_drawdown_pct',0):>6.2f}% | Sharpe: {result.get('sharpe',0):>6.3f}")
            else:
                print(f"  {strat:20s} | NO DATA / ERROR")
        except Exception as e:
            print(f"  {strat:20s} | ERROR: {e}")
