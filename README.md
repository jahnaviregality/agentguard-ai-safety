# AgentGuard: Human Oversight and Safeguard Verification

AgentGuard is a **local, reproducible research-learning prototype** for comparing two simulated approval policies for computer-use agents: approve every action, or approve sensitive actions only. It uses fictional documents, addresses and folders, and does not execute actual computer-use actions.

> **Status: prototype only.** No human-participant experiment has been conducted. The demonstration counts are not published findings or evidence of human error-detection performance.

## Features

- Six transparent, synthetic office workflow scenarios with controlled errors.
- Deterministic safeguard checks for unintended targets and missing evidence.
- Comparison of approval prompt counts and opportunities to review flagged actions.
- Optional evidence-enhanced interface for a human reviewer.
- CSV download of local reviewer decisions and standard-library unit tests.

## Run locally (Python 3.10+)

```bash
git clone https://github.com/jahnaviregality/agentguard-ai-safety.git
cd agentguard-ai-safety
python -m unittest discover -s tests -v
python -m experiments.run
python -m pip install -r requirements.txt
streamlit run app.py
```

To use this downloadable package before uploading to GitHub, extract it and run commands from its `agentguard-ai-safety` folder. On Windows, `py` may be used in place of `python`.

## Interpretation

The deterministic checker identifies rule-defined mismatches, **not** actual participant detections. In particular, a flagged action without a review prompt demonstrates a missing review opportunity, not a measured human failure. This framework does not provide real-time security protection or claim deployed-agent safety.

## Project components

- `agentguard/core.py`: scenario loading, checking, approval policies, and summaries.
- `datasets/scenarios.json`: synthetic test fixtures.
- `app.py`: local interactive approval review interface.
- `experiments/run.py`: reproducible policy summary.
- `tests/test_core.py`: unit tests.
- `research/protocol.md`: proposed study design (not conducted).
- `writing-sample.md`: technical writing sample.

## Research extension

A future within-participant pilot could counterbalance policy order, use matched tasks, and record true-positive detections, false alarms, response times and perceived workload. Obtain ethics approval as applicable before recruiting participants. Scenario design, power, and analysis procedures require validation.

## Licence

MIT (see `LICENSE`). Refer to a specific commit when citing the repository. Do not cite synthetic demonstration counts as empirical research.
