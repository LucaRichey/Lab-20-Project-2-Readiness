# Lab 20 — Project 2 Readiness

**Student:** Luca Richey | **Course:** FIN 43900 | **Date:** November 17, 2026

---

## D — The Question
> *Could a committee member who has never met you reach your decision from your repository — and does the decision survive one changed input?*

**Answer:** Yes — a stranger can read the decision numbers in [`README.md`](README.md) without running anything or reproduce them in `< 0.1s` with `python3 project2.py` (no installs needed). The decision (**Pilot, do not adopt**) survives and is strengthened under a **50 bps/yr cost drag**, which shifts **15.0 pts (\$15M)** into equities and pushes volatility from **9.44% to 11.57%** (worse than the 60/40 benchmark's 10.46%).

---

## R — Readiness Manifest (Truthful Status)

| Manifest Part | Ready Means | Status | Notes |
|---|---|:---:|---|
| **The tool** | Move one control and read the mandate verdict | Ready | [`project2.py`](project2.py) CLI flags (`--cost-bps`, `--objective`, `--equity-return`, `--ig-eq-corr`) |
| **Repository** | README with the one command producing the result | Ready | [`README.md`](README.md) → `python3 project2.py` |
| **Visible output** | Decision numbers readable on GitHub without running | Ready | In [`README.md`](README.md) and Section V below |
| **Decision memo (`docs/decision-memo.md`)** | Same numbers, dates, and conditions as output | **Open** | Final standalone `docs/decision-memo.md` to be packaged for Project 2 submission |
| **Validation & AI use** | Baseline, mandate check, stress run, Changed-Input Record | Ready | Verified in [`project2.py`](project2.py) and Section V below |
| **Videos 1–3 & transcripts** | Links work; each video answers its own question | **Open** | Not yet recorded (truthfully disclosed) |

---

## I — Cold Run (By Your Partner)

*Partner opens the repo link in their own folder, follows only [`README.md`](README.md), and writes below:*

- **Partner Name:** `_________________________`
- **Command:** `python3 project2.py`
- **First Failure (or None):** `_____________________________________________`
- **Elapsed Time:** `____________`
- **Where the Result Is:** `_____________________________________________`

---

## V — One Changed Input (Predicted First)

### Pre-Run Prediction (Committed Before Running `--cost-bps 50`)
- **Changed Input:** Annualized implementation & advisory cost drag across all four sleeves.
- **Old → New Value:** `0.00% / yr` (`0 bps`) → `0.50% / yr` (`50 bps`), lowering net Meridian returns from `3.5 / 4.3 / 5.0 / 8.0%` to `3.0 / 3.8 / 4.5 / 7.5%`.
- **Expected Direction:** Equity weight moves **UP** (to 65%–75%), bond/reserve weights move **DOWN**, and volatility rises **ABOVE** the 60/40 benchmark's `10.46%` because the baseline `6.51%` return drops to `6.01%` and fails the `6.50%` hurdle.
- **Expected Effect on Decision:** Decision (**Pilot, do not adopt**) **does not change** — it becomes stronger.

### Before Output (`python3 project2.py`)
```text
Mandate Rules   : Return >= 6.50% | Reserve >= 3.0% | Long-only
Active Inputs   : Cost Drag = 0.0 bps/yr | Net Returns = [3.5, 4.3, 5.0, 8.0]%
60/40 Benchmark : 0/0/40/60 | Return = 6.80% | Vol = 10.46% | Reserve = 0.0% (FAIL)
Baseline Mix    : 0/20/25/55 (Bills/10Y/IG/Eq) | Return = 6.51% | Vol = 9.44% | Reserve = 20.0% | PASS
Active Mix      : 0/20/25/55 (Bills/10Y/IG/Eq) | Return = 6.51% | Vol = 9.44% | Reserve = 20.0% | PASS / STABLE
Shift vs. Base  : Max weight change = 0.0 pts ($0.0M) | Vol delta = +0.00%
```

### After Output (`python3 project2.py --cost-bps 50`)
```text
Mandate Rules   : Return >= 6.50% | Reserve >= 3.0% | Long-only
Active Inputs   : Cost Drag = 50.0 bps/yr | Net Returns = [3.0, 3.8, 4.5, 7.5]%
60/40 Benchmark : 0/0/40/60 | Return = 6.80% | Vol = 10.46% | Reserve = 0.0% (FAIL)
Baseline Mix    : 0/20/25/55 (Bills/10Y/IG/Eq) | Return = 6.51% | Vol = 9.44% | Reserve = 20.0% | PASS
Active Mix      : 0/10/20/70 (Bills/10Y/IG/Eq) | Return = 6.53% | Vol = 11.57% | Reserve = 10.0% | PASS / UNSTABLE
Shift vs. Base  : Max weight change = 15.0 pts ($15.0M) | Vol delta = +2.13%
```

### What Happened & Why
- **Did the decision change?** **No** — **Pilot, do not adopt** holds and is reinforced.
- **Why it matched the prediction:** Subtracting 50 bps dropped the baseline portfolio's net return from `6.51%` to `6.01%` (infeasible). Because only equities (`7.5%` net) exceed the `6.50%` hurdle, the optimizer shifted **15.0 pts (\$15M)** from bonds into equities (`55% -> 70%`), yielding $0.10(3.8) + 0.20(4.5) + 0.70(7.5) = 6.53\%$ net return while spiking volatility by **+213 bps** (`9.44% -> 11.57%`), erasing the baseline's 102 bps risk savings versus the 60/40 benchmark (`10.46%`).

---

## Explain the Code (6-Minute Walkthrough Reference)

Core block: `search_lowest_risk_mix()` in [`project2.py`](project2.py) (lines 72–97):
1. `generate_long_only_weights(step_pct=5)` loops over all **1,771** long-only 5%-step weight combinations summing to 100%.
2. `portfolio_return(w_dec, exp_rets)` skips any mix below `6.50%` (with `1e-7` float tolerance).
3. `res_pct` sums weights of reserve-eligible sleeves (Bills + 10-Yr) and skips any mix below `3.0%`.
4. `portfolio_volatility(w_dec, cov)` computes $\sqrt{\mathbf{w}^T \mathbf{\Sigma} \mathbf{w}}$ and keeps the lowest-volatility passing mix (or returns `None` if infeasible).
5. `run()` subtracts `cost_bps / 100.0`, compares against baseline, and flags `PASS / UNSTABLE` if max weight shift $\ge 10$ pts.

---

## E — Fix One Thing

- **First failure found pre-fix:** Prior workspace had multiple lab scripts with no `README.md`, no one-command runner, and external package dependencies (`pandas`/`streamlit`) that could fail on a cold machine.
- **Fix applied:** Consolidated the decision engine into one zero-dependency script ([`project2.py`](project2.py)) with a short [`README.md`](README.md) showing the exact command and visible output.
- **Re-test:** Cold run of `python3 project2.py` completes with exit code `0` in `< 0.1s`. *(Update if partner hits any error during live cold run.)*

---

## Your Decision Line

> **Pilot, do not adopt**, the Meridian lowest-risk allocation (`0/20/25/55`; **6.51%** return, **9.44%** volatility, **20.0%** reserve-eligible) — and reverse to **adopt** only if the Investment Committee sets a **40%–65% equity band**, approves shrinkage priors keeping max weight shifts under **10 percentage points** under a **50 bps cost drag** or **100 bps equity shock**, and defines the CIO's calendar-year drawdown limit (Statement S9).

---

## Reflect

1. **What the cold run found that I could not see:** Working scripts from earlier labs aren't enough on their own — a stranger needs one short README, one zero-friction command, and visible numbers upfront to reach the decision without coaching.
2. **What I will not touch before the deadline:** The core mandate/volatility math in `project2.py`, the baseline Meridian inputs, and the `Pilot, do not adopt` decision line and reversal conditions.
