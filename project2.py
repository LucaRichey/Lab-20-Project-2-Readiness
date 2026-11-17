#!/usr/bin/env python3
"""
project2.py — Meridian Foundation Reserve ($100M) Decision Engine
Author: Luca Richey | FIN 43900 (Purdue University) | Lab 20

Self-contained (Python standard library only). No pip install required.
Usage:
  python3 project2.py                # Baseline (0 bps cost drag)
  python3 project2.py --cost-bps 50  # Changed-input run (50 bps/yr cost drag)
"""

import argparse
import math

# ==============================================================================
# MERIDIAN INPUTS
# ==============================================================================
RESERVE_SIZE = 100.0          # $100M portfolio
QUARTERLY_DISTRIBUTION = 0.75 # $0.75M/quarter
QUARTERS_TO_COVER = 4         # 12 months -> 3.0% minimum reserve
OBJECTIVE_RETURN = 6.5        # CPI 2.5% + 4.0% net real return

SLEEVES = [
    {"name": "Bills",   "expected_return": 3.5, "volatility": 0.5,  "reserve_eligible": True},
    {"name": "10-Yr",   "expected_return": 4.3, "volatility": 7.0,  "reserve_eligible": True},
    {"name": "IG Bond", "expected_return": 5.0, "volatility": 6.0,  "reserve_eligible": False},
    {"name": "Equity",  "expected_return": 8.0, "volatility": 16.0, "reserve_eligible": False},
]

# Order: [Bills, 10-Yr, IG Bond, Equity]
CORRELATION_MATRIX = [
    [1.00,  0.10,  0.05,  0.00],
    [0.10,  1.00,  0.80, -0.10],
    [0.05,  0.80,  1.00,  0.25],
    [0.00, -0.10,  0.25,  1.00],
]


# ==============================================================================
# CORE MATH & MANDATE-CONSTRAINED SEARCH
# ==============================================================================
def validate_correlation_matrix(corr):
    n = len(corr)
    for i in range(n):
        if abs(corr[i][i] - 1.0) > 1e-6:
            raise ValueError(f"Diagonal ({i},{i}) must be 1.0")
        for j in range(n):
            if not (-1.0 <= corr[i][j] <= 1.0):
                raise ValueError(f"Correlation ({i},{j}) out of [-1, 1]")
            if abs(corr[i][j] - corr[j][i]) > 1e-6:
                raise ValueError(f"Correlation matrix not symmetric at ({i},{j})")


def build_covariance(corr, vols):
    n = len(vols)
    return [[corr[i][j] * vols[i] * vols[j] for j in range(n)] for i in range(n)]


def portfolio_return(w_dec, exp_rets):
    return sum(w * r for w, r in zip(w_dec, exp_rets))


def portfolio_volatility(w_dec, cov):
    var = sum(w_dec[i] * cov[i][j] * w_dec[j] for i in range(len(w_dec)) for j in range(len(w_dec)))
    return math.sqrt(max(var, 0.0))


def generate_long_only_weights(step_pct=5):
    """All 1,771 four-asset long-only portfolios in 5-point steps summing to 100%."""
    steps = 100 // step_pct
    combos = []
    for a in range(steps + 1):
        for b in range(steps - a + 1):
            for c in range(steps - a - b + 1):
                d = steps - a - b - c
                combos.append([a * step_pct, b * step_pct, c * step_pct, d * step_pct])
    return combos


def search_lowest_risk_mix(exp_rets, cov, reserve_flags, objective=6.5, min_reserve=3.0):
    """Return the lowest-volatility feasible mix meeting return and reserve rules."""
    best = None
    min_vol = float("inf")
    tol = 1e-7

    for w_pct in generate_long_only_weights(step_pct=5):
        w_dec = [w / 100.0 for w in w_pct]

        ret = portfolio_return(w_dec, exp_rets)
        if ret < objective - tol:
            continue

        res_pct = sum(w for w, flag in zip(w_pct, reserve_flags) if flag)
        if res_pct < min_reserve - tol:
            continue

        vol = portfolio_volatility(w_dec, cov)
        if vol < min_vol - 1e-9:
            min_vol = vol
            best = {
                "weights": w_pct,
                "return": ret,
                "volatility": vol,
                "reserve": res_pct,
            }
    return best


def run(cost_bps=0.0, objective=OBJECTIVE_RETURN, equity_return=None, ig_eq_corr=0.25):
    min_reserve = (QUARTERS_TO_COVER * QUARTERLY_DISTRIBUTION / RESERVE_SIZE) * 100.0
    vols = [s["volatility"] for s in SLEEVES]
    flags = [s["reserve_eligible"] for s in SLEEVES]
    base_rets = [s["expected_return"] for s in SLEEVES]

    validate_correlation_matrix(CORRELATION_MATRIX)
    base_cov = build_covariance(CORRELATION_MATRIX, vols)
    baseline = search_lowest_risk_mix(base_rets, base_cov, flags, OBJECTIVE_RETURN, min_reserve)

    # 60/40 policy benchmark (0% Bills, 0% 10-Yr, 40% IG, 60% Equity)
    bench_w = [0.0, 0.0, 0.40, 0.60]
    bench_ret = portfolio_return(bench_w, base_rets)
    bench_vol = portfolio_volatility(bench_w, base_cov)

    # Active run (with optional cost drag / stress overrides)
    corr = [row[:] for row in CORRELATION_MATRIX]
    corr[2][3] = corr[3][2] = ig_eq_corr
    validate_correlation_matrix(corr)
    cov = build_covariance(corr, vols)

    rets = base_rets[:]
    if equity_return is not None:
        rets[3] = equity_return
    net_rets = [r - cost_bps / 100.0 for r in rets]
    active = search_lowest_risk_mix(net_rets, cov, flags, objective, min_reserve)

    print("=" * 78)
    print("MERIDIAN FOUNDATION RESERVE ($100M) — PROJECT 2 DECISION OUTPUT")
    print("=" * 78)
    print(f"Mandate Rules   : Return >= {objective:.2f}% | Reserve >= {min_reserve:.1f}% | Long-only")
    print(f"Active Inputs   : Cost Drag = {cost_bps:.1f} bps/yr | Net Returns = {[round(r, 2) for r in net_rets]}%")
    print(f"60/40 Benchmark : 0/0/40/60 | Return = {bench_ret:.2f}% | Vol = {bench_vol:.2f}% | Reserve = 0.0% (FAIL)")
    print("-" * 78)
    print(f"Baseline Mix    : {'/'.join(str(w) for w in baseline['weights'])} (Bills/10Y/IG/Eq) | "
          f"Return = {baseline['return']:.2f}% | Vol = {baseline['volatility']:.2f}% | "
          f"Reserve = {baseline['reserve']:.1f}% | PASS")

    if active is None:
        print("Active Mix      : INFEASIBLE — no mix meets objective and reserve rules (FAIL)")
    else:
        shifts = [abs(a - b) for a, b in zip(active["weights"], baseline["weights"])]
        max_shift = max(shifts)
        verdict = "PASS / UNSTABLE" if max_shift >= 10 else "PASS / STABLE"
        print(f"Active Mix      : {'/'.join(str(w) for w in active['weights'])} (Bills/10Y/IG/Eq) | "
              f"Return = {active['return']:.2f}% | Vol = {active['volatility']:.2f}% | "
              f"Reserve = {active['reserve']:.1f}% | {verdict}")
        print(f"Shift vs. Base  : Max weight change = {max_shift:.1f} pts (${max_shift:.1f}M) | "
              f"Vol delta = {active['volatility'] - baseline['volatility']:+.2f}%")

    print("-" * 78)
    print("DECISION LINE:")
    print("  Pilot, do not adopt, the Meridian lowest-risk allocation (0/20/25/55; 6.51%")
    print("  return, 9.44% vol, 20.0% reserve) — reverse to adopt only if the committee")
    print("  sets a 40%-65% equity band, approves shrinkage priors keeping max weight")
    print("  shifts under 10 pts under a 50 bps cost drag or 100 bps equity shock, and")
    print("  defines the CIO's calendar-year drawdown limit (S9).")
    print("=" * 78)


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--cost-bps", type=float, default=0.0, help="Annual cost drag in bps (default: 0)")
    p.add_argument("--objective", type=float, default=OBJECTIVE_RETURN, help="Return hurdle % (default: 6.5)")
    p.add_argument("--equity-return", type=float, default=None, help="Override equity return %")
    p.add_argument("--ig-eq-corr", type=float, default=0.25, help="IG-Equity correlation (default: 0.25)")
    args = p.parse_args()
    run(args.cost_bps, args.objective, args.equity_return, args.ig_eq_corr)
