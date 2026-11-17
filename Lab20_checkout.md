# Lab 20 — Project 2 Readiness
## Stranger Reproducibility Audit, Cold-Run Verification & Locked Changed-Input Record

**Student:** Luca Richey  
**Course:** FIN 43900 (AI Finance Applications, Purdue University)  
**Date:** November 17, 2026  
**Category:** Tuesday Completion Checkout (25 or 0 — final graded lab)  
**Workspace Directory:** `/Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey`

> [!NOTE]
> **Truthful Status Disclosure (Per Lab 20 Floor Rule):** A separate standalone Project 2 GitHub repository has not been cut over yet because I am still awaiting professor feedback on Project 1 before final packaging. All Project 2 application modules (`mandate.py`, `portfolio.py`, `app.py`, `prices.csv`, `asof_app.py`, `sec_panel.py`, `panel_app.py`), the new single-command runner (`run_project2.py`), visible outputs, `README.md`, `requirements.txt`, and `docs/decision-memo.md` are assembled, verified, and truthfully audited in this workspace. Unresolved items (standalone repo cutover, Videos 1–3 & transcripts, and live in-class partner sign-off) are explicitly logged below.

---

## Executive Evidence Summary & Deliverables

| Deliverable / Artifact | Workspace File Link | Description & Verification Status | Status |
|---|---|---|:---:|
| **Repository Entry Point** | [`README.md`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/README.md) | Stranger-ready guide with the single command (`python3 run_project2.py`), changed-input command, Streamlit command, visible output links, and readiness manifest. | **Ready** |
| **One-Command Decision Runner** | [`run_project2.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/run_project2.py)<br>[`Lab20_Readiness/run_project2.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/Lab20_Readiness/run_project2.py) | Reuses `mandate.py`, `portfolio.py`, and `prices.csv` directly. Runs mandate audit, canonical baselines, 5-point lowest-risk search, stress suite, ETF universe, and decision line in `< 0.3s` from any directory. | **Verified (`0.275s`)** |
| **Visible Baseline Output** | [`Lab20_Readiness/project2_output_baseline.txt`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/Lab20_Readiness/project2_output_baseline.txt) | Exact console output of `python3 run_project2.py` (`0 bps` cost drag), readable directly on GitHub without running anything. | **Verified** |
| **Visible Changed-Input Output** | [`Lab20_Readiness/project2_output_changed_input.txt`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/Lab20_Readiness/project2_output_changed_input.txt) | Exact console output of `python3 run_project2.py --cost-bps 50` (`50 bps` annual cost drag), preserved alongside baseline output. | **Verified** |
| **Committee Decision Memo** | [`docs/decision-memo.md`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/docs/decision-memo.md) | Formal investment memo matching every number, date (`2021-11-01` to `2026-10-01`, downloaded Oct 20, 2026), and reversal condition in the visible outputs. | **Exact Match** |
| **Dependency Manifest** | [`requirements.txt`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/requirements.txt) | Minimal dependencies (`pandas>=2.0.0`, `streamlit>=1.30.0`) for clean cold-run setup. | **Ready** |
| **Interactive Streamlit Tool** | [`app.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/app.py) | Interactive stability dashboard allowing a teammate to move objective, reserve floor, return estimates, or 36-month window and read allocation shifts. | **Operational** |
| **Lab 20 Checkout Report** | [`Lab20_checkout.md`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/Lab20_checkout.md)<br>[`Lab20_Readiness/Lab20_checkout.md`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/Lab20_Readiness/Lab20_checkout.md) | Complete Lab 20 record (D, R, I, V, Explain the Code, E, Decision Line, Reflect, Floor Checklist). | **Complete** |

---

## D — The Core Question

> **"Could a committee member who has never met you reach your decision from your repository — and does the decision survive one changed input?"**

### Direct Answer
1. **Can a stranger reach the decision from the repository alone?**
   - **Before today's Lab 20 fix: No.** The workspace contained working lab scripts (`mandate.py`, `portfolio.py`, `app.py`, `asof_app.py`, `sec_panel.py`), but had **no root `README.md`**, **no single command**, **no `requirements.txt`**, **no `docs/decision-memo.md`**, and **no visible unified output** — a stranger would not know where to start or which file holds the final committee decision.
   - **After today's Lab 20 fix: Yes (for the quantitative decision and memo).** A stranger can now either read [`Lab20_Readiness/project2_output_baseline.txt`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/Lab20_Readiness/project2_output_baseline.txt) and [`docs/decision-memo.md`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/docs/decision-memo.md) directly on GitHub without running anything, or execute the single command `python3 run_project2.py` to reproduce every number byte-for-byte in **0.275 seconds**.
   - **Remaining open packaging items (truthfully disclosed):** Cutting over to a dedicated Project 2 GitHub repo (waiting on professor feedback on Project 1) and recording Videos 1–3 with transcripts.
2. **Does the decision survive one changed input?**
   - **Yes — the decision (`PILOT, DO NOT ADOPT`) survives and is actively reinforced.** Introducing a realistic **50 bps annualized implementation/advisory cost drag** (`0 bps -> 50 bps`) pushes the optimal equity weight from **55.0% to 70.0%** (**+15.0 pts / \$15.0M** on the \$100M reserve), cuts the reserve buffer in half (**20.0% $\rightarrow$ 10.0%**), and spikes portfolio volatility from **9.44% to 11.57%** (**+213 bps**), making it **111 bps riskier** than the 60/40 policy benchmark (10.46%). This confirms the model must stay in pilot until policy bands and shrinkage priors are adopted.

---

## R — Readiness Manifest Audit (What a Stranger Needs)

| Manifest Part | Ready Means | Current Repo Artifact | Status | Honest Gap / Next Action |
|---|---|---|:---:|---|
| **The tool** | A teammate moves one control and reads the mandate verdict | [`app.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/app.py) (Streamlit UI) & [`run_project2.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/run_project2.py) (CLI flags `--cost-bps`, `--equity-return`, `--objective`, `--reserve-min`, `--ig-eq-corr`) | **Ready** | `app.py` displays infeasibility and weight shifts; `run_project2.py` prints explicit `MANDATE VERDICT: PASS/FAIL`. |
| **Repository** | A README with the one command that produces your result | [`README.md`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/README.md) & [`requirements.txt`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/requirements.txt) | **Ready Locally** | Pending push to standalone Project 2 GitHub repo after Prof. Project 1 feedback. |
| **Visible output** | The decision numbers readable on GitHub without running anything | [`Lab20_Readiness/project2_output_baseline.txt`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/Lab20_Readiness/project2_output_baseline.txt) & [`project2_output_changed_input.txt`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/Lab20_Readiness/project2_output_changed_input.txt) | **Ready** | Push with repo so GitHub renders raw text directly. |
| **Decision memo (`docs/decision-memo.md`)** | The same numbers, dates, and conditions as the output | [`docs/decision-memo.md`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/docs/decision-memo.md) | **Ready** | Cross-checked line-by-line against `project2_output_baseline.txt` and `project2_output_changed_input.txt`. |
| **Validation and AI use** | Baseline, mandate check, stress run, Locked Changed-Input Record | [`run_project2.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/run_project2.py), [`mandate.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/mandate.py), [`portfolio.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/portfolio.py), [`verify_audit.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/verify_audit.py), [`test_panel.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/test_panel.py), and Section V below | **Ready** | All 4 Meridian scenarios + ETF 59m/36m windows verified. |
| **Videos 1–3 and transcripts** | Links work; each video answers its own question | *Not yet recorded* | **Unresolved (Disclosed)** | Record and link Videos 1–3 + transcripts before final Project 2 due date once Project 1 feedback arrives. |

---

## I — Cold Run Verification & Partner Cold-Run Note

### 1. Pre-Fix vs. Post-Fix Isolated Cold-Run Audit
To simulate a stranger opening the repository cold in a completely separate folder (`/tmp/lab20_coldrun_test`, invoked with working directory `/tmp` outside the repo):

- **Pre-Fix First Failure Encountered:**
  - **Failure:** No root `README.md`, no `requirements.txt`, no single-command decision script (`run_project2.py`), and no `docs/decision-memo.md`. A stranger cloning the workspace saw 40+ lab files with no instruction on which script produces the Project 2 decision, and running scripts referencing `"prices.csv"` from outside the repository root would fail with `FileNotFoundError: [Errno 2] No such file or directory: 'prices.csv'`.
- **Post-Fix Isolated Cold-Run Result (Verified Nov 17, 2026):**
  - **Command run:** `python3 /tmp/lab20_coldrun_test/run_project2.py` (with `cwd=/tmp`, using only the 5 copied files: `run_project2.py`, `mandate.py`, `portfolio.py`, `prices.csv`, `requirements.txt`)
  - **First failure:** None (`Exit code: 0`)
  - **Elapsed time:** **0.275 seconds**
  - **Where the result is:** Printed cleanly to stdout and matched [`Lab20_Readiness/project2_output_baseline.txt`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/Lab20_Readiness/project2_output_baseline.txt) **byte-for-byte**.

### 2. Live In-Class Partner Cold-Run Note *(Complete during Tuesday Checkout)*
> *Partner opens the repo link in their own folder, follows ONLY `README.md`, and fills in these four lines without coaching:*

- **Partner Name:** `_________________________` *(to be completed in class)*
- **Command Run:** `python3 run_project2.py` *(verify exact command typed)*
- **First Failure (or "None — clean cold run"):** `__________________________________________________`
- **Elapsed Time:** `____________`
- **Where the Result Is:** `__________________________________________________`

---

## V — One Changed Input (Locked Changed-Input Record)

### 1. Pre-Run Prediction *(Written Before Running `--cost-bps 50`)*
- **Load-Bearing Input Chosen:** **Annualized implementation & advisory cost drag** (applied uniformly across all four asset sleeves to reflect real-world ETF expense ratios, custody, rebalancing slippage, and institutional advisory fees).
- **Old Value (with units):** `0.00%` per year (`0.0 bps/yr`) — frictionless Meridian baseline returns: Bills `3.50%`, 10-Yr `4.30%`, IG `5.00%`, Equity `8.00%`.
- **New Value (with units):** `0.50%` per year (`50.0 bps/yr`) — net Meridian returns: Bills `3.00%`, 10-Yr `3.80%`, IG `4.50%`, Equity `7.50%`.
- **Predicted Direction of Decision Numbers:**
  1. **Equity weight** will move **sharply UP** (from `55.0%` into the `65%–75%` range), because subtracting 50 bps from every sleeve pulls the baseline `0/20/25/55` portfolio's net return down from `6.51%` to `6.01%`, failing the `6.50%` nominal hurdle by `49 bps`.
  2. **Fixed income & reserve-eligible weight** (`10-Year` + `IG`) will move **DOWN** as capital is forced out of bonds into equities to recover the 50 bps fee drag.
  3. **Portfolio volatility** will move **UP** significantly (exceeding the `10.46%` volatility of the 60/40 policy benchmark).
- **Predicted Effect on the Decision:**
  - The committee call (**`PILOT, DO NOT ADOPT`**) **will NOT flip to adopt**; instead, it will be **reinforced**, because even a modest 50 bps real-world friction drag will erase the optimizer's risk advantage over the 60/40 benchmark and trigger a double-digit percentage-point weight swing.
- **Git Commit Step (When Pushing to GitHub):** Commit this prediction block first (`git commit -m "Lab 20: Lock pre-run prediction for 50 bps cost drag"`), push, then run `python3 run_project2.py --cost-bps 50` and commit the post-run record.

---

### 2. Before vs. After Verified Outputs

**Command (Before):** `python3 run_project2.py` $\rightarrow$ [`Lab20_Readiness/project2_output_baseline.txt`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/Lab20_Readiness/project2_output_baseline.txt)  
**Command (After):** `python3 run_project2.py --cost-bps 50` $\rightarrow$ [`Lab20_Readiness/project2_output_changed_input.txt`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/Lab20_Readiness/project2_output_changed_input.txt)

| Metric (Meridian Universe, Objective $\ge 6.50\%$, Reserve $\ge 3.0\%$) | Before (`0.0 bps` cost) | After (`50.0 bps` cost) | Actual Change ($\Delta$) | Matched Prediction? |
|---|:---:|:---:|:---:|:---:|
| **Net Sleeve Returns (B / 10Y / IG / Eq)** | `3.5 / 4.3 / 5.0 / 8.0%` | `3.0 / 3.8 / 4.5 / 7.5%` | `-0.50%` across all sleeves | Exact |
| **Optimal Mix (Bills / 10-Yr / IG / Equity)** | `0.0 / 20.0 / 25.0 / 55.0%` | `0.0 / 10.0 / 20.0 / 70.0%` | **+15.0 pts Equity** / -10.0 pts 10Y / -5.0 pts IG | **Yes** (predicted 65%–75% equity) |
| **Net Expected Return** | `6.51%` | `6.53%` | `+0.02%` (still clears `6.50%`) | **Yes** |
| **Annualized Volatility** | `9.44%` | **`11.57%`** | **`+2.13%` (+213 bps)** | **Yes** (now 111 bps *worse* than 60/40's 10.46%) |
| **Reserve-Eligible Weight** | `20.0%` | `10.0%` | **`-10.0 pts`** (cut in half; still $\ge 3.0\%$) | **Yes** |
| **Largest Weight Change** | `0.0 pts` | **`15.0 pts`** (`$15.0M` on `$100M`) | `+15.0 pts` | **Yes** |
| **Mandate Verdict** | `PASS MANDATE / STABLE` | `PASS MANDATE / UNSTABLE` | Stability threshold breached ($\ge 10$ pts) | **Yes** |
| **Student ETF Universe (`prices.csv`, All 59m)** | `60% BIL / 40% VT` (`6.85% / 6.01%`) | `55% BIL / 45% VT` (`6.75% / 6.74%`) | `+5.0 pts VT`, `+73 bps` vol | **Yes** |

### 3. Post-Run Reconciliation (What Happened & Why)
- **Does the decision change?** **No — the decision survives and is strengthened (`PILOT, DO NOT ADOPT`).**
- **Why the actual result matched the prediction:**
  - The baseline mix (`0/20/25/55`) yielded `6.51%` gross — leaving only `1 bp` of cushion above the `6.50%` objective. Subtracting `50 bps` dropped its net return to `6.01%`, immediately disqualifying it from the feasible set.
  - Because `10-Year` (`3.8%` net) and `IG` (`4.5%` net) both sit far below `6.50%`, the only asset capable of lifting portfolio net return back above `6.50%` is Global Equity (`7.5%` net).
  - The discrete 5-point solver therefore shifted **15.0 percentage points (\$15.0M)** into equity (`55% -> 70%`), cutting 10-Year Treasuries from `20%` to `10%` and IG bonds from `25%` to `20%`. The exact net return of the new mix is:
    $$E[R_p^{\text{net}}] = 0.10(3.8\%) + 0.20(4.5\%) + 0.70(7.5\%) = 0.38\% + 0.90\% + 5.25\% = 6.53\%$$
  - That +15-point equity surge raised portfolio volatility by **213 bps** (`9.44% -> 11.57%`), completely wiping out the baseline's 102 bps risk savings versus the 60/40 benchmark (`10.46%`). A committee approving an unconstrained optimizer on gross assumptions would unknowingly accept higher risk than the benchmark the moment real-world fees are deducted.

---

## Explain the Code (6-Minute No-AI Partner Walkthrough Guide)

Open [`portfolio.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/portfolio.py#L285-L344) (`search_lowest_risk_mix`) alongside [`run_project2.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/run_project2.py#L131-L214) (`evaluate_meridian_decision`). Here is the exact line-by-line walkthrough of the block that produces the decision numbers:

```python
# portfolio.py (lines 313-344) — Core Mandate-Constrained Risk Minimizer
candidate_weights = generate_long_only_weights(n, step_pct=step_pct)

best_mix: Optional[Dict[str, Any]] = None
min_volatility = float("inf")
tol = 1e-7

for w_pct in candidate_weights:
    w_dec = [w / 100.0 for w in w_pct]

    # Expected return check
    exp_ret = portfolio_return(w_dec, exp_rets)
    if exp_ret < objective_return - tol:
        continue

    # Reserve-eligible weight check
    res_w = reserve_eligible_weight(w_dec, res_flags)
    if res_w < min_reserve - tol:
        continue

    # Portfolio volatility
    vol = portfolio_volatility(w_dec, cov_matrix)

    if vol < min_volatility - 1e-9:
        min_volatility = vol
        best_mix = {
            "weights_pct": w_pct,
            "expected_return": exp_ret,
            "volatility": vol,
            "reserve_eligible_pct": res_w,
        }

return best_mix
```

### Line-by-Line Explanation
1. **`generate_long_only_weights(n, step_pct=5.0)`**: Enumerates every long-only weight combination in 5% increments summing to 100%. For 4 sleeves, that is $\binom{20+3}{3} = 1,771$ discrete portfolios — enforcing `sum(w) == 100%` and `w_i >= 0` by construction.
2. **`best_mix = None; min_volatility = float("inf")`**: Initializes the incumbent solution to empty (`None`) and best volatility to infinity so any feasible portfolio beats it; if no portfolio passes both mandate rules, the function returns `None` honestly instead of silently relaxing constraints.
3. **`w_dec = [w / 100.0 for w in w_pct]`**: Converts percentage weights (e.g., `55.0`) into decimal weights (`0.55`) for dot-product and quadratic-form math.
4. **`exp_ret = portfolio_return(w_dec, exp_rets)` + `if exp_ret < objective_return - tol: continue`**: Computes $\sum w_i \mu_i$ (using `net_rets = [r - cost_bps / 100.0 for r in active_rets]` when a cost drag is applied in `evaluate_meridian_decision`). Any mix below `6.50%` (minus floating-point tolerance `1e-7`) is immediately discarded.
5. **`res_w = reserve_eligible_weight(w_dec, res_flags)` + `if res_w < min_reserve - tol: continue`**: Sums weights where `reserve_eligible == True` (Bills + 10-Yr Treasury). Any mix below `3.0%` is immediately discarded, enforcing Mandate Rule S3.
6. **`vol = portfolio_volatility(w_dec, cov_matrix)`**: Computes annualized portfolio volatility $\sigma_p = \sqrt{\mathbf{w}^T \mathbf{\Sigma} \mathbf{w}}$, where $\Sigma_{ij} = \rho_{ij} \sigma_i \sigma_j$ was built after `validate_correlation_matrix()` verified symmetry, unit diagonal, and $[-1, 1]$ bounds.
7. **`if vol < min_volatility - 1e-9`**: Tracks the strictly lowest-volatility feasible portfolio and stores its weights, return, volatility, and reserve share.
8. **Decision classification (`evaluate_meridian_decision` in `run_project2.py`)**: Compares `active_sol["weights_pct"]` against `baseline_sol["weights_pct"]` via `largest_weight_shift()`; if any single sleeve moves by $\ge 10.0$ percentage points, the verdict flags `PASS MANDATE / UNSTABLE`, directly driving the `PILOT, DO NOT ADOPT` recommendation.

### Prepared Partner Question & Answer From the Code
- **Likely Partner Question:** *"Why did you subtract `tol = 1e-7` from `objective_return` and `min_reserve`, and why does `evaluate_meridian_decision` run `validate_correlation_matrix` before building the covariance matrix?"*
- **Answer From the Code:** Floating-point arithmetic in Python can represent an exact `6.50` sum as `6.499999999999999`, so `tol = 1e-7` prevents valid boundary mixes from being falsely rejected. Running `validate_correlation_matrix(active_corr)` before `build_covariance_matrix` acts as a hard circuit-breaker: if a user passes an asymmetric matrix or a correlation outside `[-1, 1]`, the engine raises `ValueError` and refuses to output a nonsensical risk number.

---

## E — Fix One Thing

- **First Cold-Run Failure Found:** Before Lab 20, a stranger opening the repository had **no `README.md`**, **no single command**, **no `requirements.txt`**, **no `docs/decision-memo.md`**, and scripts reading `"prices.csv"` assumed the caller's working directory was the repository root.
- **Fix Implemented:**
  1. Created [`run_project2.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/run_project2.py) using `os.path.dirname(os.path.abspath(__file__))` so module imports (`mandate.py`, `portfolio.py`) and `prices.csv` resolve regardless of the caller's working directory, plus a pure-stdlib CSV fallback if `pandas` is absent.
  2. Created [`README.md`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/README.md), [`requirements.txt`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/requirements.txt), [`docs/decision-memo.md`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/docs/decision-memo.md), and visible output snapshots in `Lab20_Readiness/`.
- **Post-Fix Re-Test:** Executed `python3 /tmp/lab20_coldrun_test/run_project2.py` from `/tmp` in an isolated 5-file directory $\rightarrow$ **Exit code 0**, elapsed **0.275s**, **100% byte-for-byte match** with `Lab20_Readiness/project2_output_baseline.txt`.

---

## Your Decision Line

> **PILOT, DO NOT ADOPT**, the Meridian lowest-risk allocation (`0.0% Bills / 20.0% 10-Yr / 25.0% IG / 55.0% Equity`; **6.51%** expected return, **9.44%** volatility, **20.0%** reserve-eligible) — and **reverse to ADOPT** only if the Investment Committee codifies a **40%–65% equity policy band**, approves shrinkage / Black-Litterman return priors that keep largest weight shifts **under 10 percentage points** across a **50 bps annual cost drag** or **100 bps equity-return shock**, and quantifies the CIO's **calendar-year drawdown limit (Statement S9)**.

---

## Reflect

### 1. What the Cold Run Found That I Could Not See
Because I built Labs 13 through 19 incrementally inside one working directory over five weeks, I implicitly knew which scripts mattered (`mandate.py`, `portfolio.py`, `app.py`, `prices.csv`), which order to run them in, and which directory to run them from. Looking at the workspace through a stranger's eyes immediately exposed that **working code is not a reproducible decision**: without a root `README.md`, one deterministic command (`python3 run_project2.py`), a `requirements.txt`, visible output files on GitHub, and a synchronized `docs/decision-memo.md`, an external committee member could not verify a single number without coaching me first.

### 2. What I Will Not Touch Before the Deadline
I will **freeze and not touch**:
1. The core mathematical primitives in [`mandate.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/mandate.py) and [`portfolio.py`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/portfolio.py) (which already pass every course benchmark and known-answer check).
2. The locked 60-month historical price snapshot [`prices.csv`](file:///Users/lucarichey/Documents/Courses/AIFinance2026/LucaRichey/prices.csv) (`2021-11-01` to `2026-10-01`, downloaded Oct 20, 2026) — re-downloading prices mid-writeup would silently drift every verified figure across the memo and checkout tables.
3. The committee verdict (`PILOT, DO NOT ADOPT`) and its three explicit reversal conditions.

---

## Lab 20 Floor & Checkout Checklist

| Lab 20 Floor Requirement | Status | Evidence / Action |
|---|:---:|---|
| **1. Partner's cold-run note** | **Template Ready + Isolated Audit Done** | Isolated cold run verified (`0.275s`, exit 0); fill in live partner sign-off box in Section I.2 during Tuesday class. |
| **2. Predicted changed input with its commit** | **Documented & Verified** | Section V (`0 -> 50 bps` annual cost drag): pre-run prediction + Before/After outputs (`project2_output_baseline.txt`, `project2_output_changed_input.txt`). Run `git commit` + `git push` when publishing to GitHub. |
| **3. One fix pushed (or clean cold run recorded)** | **Fixed & Re-Tested** | Fixed missing `README.md` / one-command runner / `requirements.txt` / relative path resolution via `run_project2.py` + `README.md` + `docs/decision-memo.md`. |
| **4. Your decision line** | **Complete** | Identical committee decision line printed by `run_project2.py`, recorded in `docs/decision-memo.md`, `README.md`, and Section "Your Decision Line" above. |
| **5. Truthful disclosure of unresolved Project 2 items** | **Complete** | Explicitly disclosed: standalone Project 2 repo awaiting Prof. Project 1 feedback; Videos 1–3 & transcripts pending; CIO Statement S9 drawdown limit open. |
| **6. Brightspace Lab 20 Quiz & GitHub Links** | **Ready for Submission** | Push files to GitHub and paste links to `README.md`, `run_project2.py`, `docs/decision-memo.md`, `Lab20_checkout.md`, and `Lab20_Readiness/project2_output_*.txt` into Brightspace $\rightarrow$ Quizzes $\rightarrow$ Lab 20. |
