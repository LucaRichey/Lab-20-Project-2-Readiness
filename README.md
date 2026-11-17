# Meridian Foundation Reserve (\$100M) — Lab 20 / Project 2 Readiness

**Student:** Luca Richey | **Course:** FIN 43900 (Purdue University)

## One Command to Run

Python 3 standard library only (no `pip install` required):

```bash
python3 project2.py
```

Changed-input run (`50 bps/yr` cost drag):

```bash
python3 project2.py --cost-bps 50
```

## Visible Decision Output (Readable Without Running)

| Run (Objective $\ge 6.50\%$, Reserve $\ge 3.0\%$) | Mix (Bills / 10-Yr / IG / Eq) | Return | Volatility | Reserve | Max Shift | Verdict |
|---|:---:|:---:|:---:|:---:|:---:|---|
| **60/40 Benchmark** | `0 / 0 / 40 / 60` | 6.80% | 10.46% | 0.0% | — | **FAIL** (reserve < 3%) |
| **Baseline (`0 bps` cost)** | `0 / 20 / 25 / 55` | **6.51%** | **9.44%** | **20.0%** | 0.0 pts | **PASS / STABLE** |
| **Changed Input (`50 bps` cost)** | `0 / 10 / 20 / 70` | 6.53% | **11.57%** | 10.0% | **15.0 pts** | **PASS / UNSTABLE** |

**Decision Line:** **Pilot, do not adopt**, the Meridian lowest-risk allocation (`0/20/25/55`; 6.51% return, 9.44% volatility, 20.0% reserve-eligible) — reverse to **adopt** only if the committee sets a 40%–65% equity band, approves shrinkage priors keeping max weight shifts under 10 pts under a 50 bps cost drag or 100 bps equity shock, and defines the CIO's calendar-year drawdown limit (S9).

## Files in This Repository
- [`README.md`](README.md) — One-command instructions and visible decision output.
- [`project2.py`](project2.py) — Self-contained decision engine (standard library only).
- [`Lab20_checkout.md`](Lab20_checkout.md) — Lab 20 readiness check, partner cold-run note, changed-input record, fix, decision line, and reflection.
