# Adversarial Game Agents

A Pygame game environment with random, greedy, MaxN, Minimax, and alpha-beta Minimax agents.

## Run

Requires Python 3 and a graphical desktop.

```sh
python -m venv .venv
# Activate .venv using the command appropriate for your shell.
python -m pip install -r requirements.txt
python main.py RandomAgent example_map.txt
```

Command-line arguments, in order:

1. Comma-separated agent class names (choose the number required by the map).
2. Map filename from `maps/`.
3. Maximum rounds (default 5).
4. Maximum elapsed time (default 0).
5. Search depth (default 5).
6. Optional debug argument. The original implementation uses Python's `bool(string)`, so any nonempty string, including `False`, evaluates to true.

Run from the repository root. `agents.py` contains the agent implementations; `state.py` provides legal actions, successor states, and scores. GUI behavior and agent correctness require further testing.

## Context

Educational project by Marko Mijanovic, University of Belgrade, School of Electrical Engineering. Course scaffolding and supplied assets remain part of the project; this preparation does not grant a new license to third-party material.

## Preparation validation

- AST syntax check for 7 Python files: passed.

Pygame runtime and algorithm correctness were not tested. Dependency versions are intentionally unpinned until a runtime test establishes a compatible set.
