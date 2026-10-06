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
6. Debug mode (default `true`). Accepts `true`/`false`, `1`/`0`, `yes`/`no`, or `on`/`off`, case-insensitively.

Run from the repository root. `agents.py` contains the agent implementations; `state.py` provides legal actions, successor states, and scores. GUI behavior and agent correctness require further testing.

## Agent comparison

| Agent | Decision rule |
|---|---|
| `RandomAgent` | Random legal action |
| `GreedyAgent` | Immediate evaluation |
| `MaxNAgent` | Multiplayer score-vector search |
| `MinimaxAgent` | Adversarial tree search |
| `MinimaxABAgent` | Minimax with alpha-beta pruning |

Run `python main.py --help` without starting the GUI. For example, `python main.py RandomAgent example_map.txt 5 0 5 false` disables debug output.

## Command-line tests

Run `python -m unittest discover -s tests -v`. These standard-library tests verify Boolean parsing and the original positional interface without requiring Pygame or a monitor. They do not exercise the game engine or establish agent optimality.

## Context

Educational project by [Marko Mijanovic](https://github.com/markomijanovic), University of Belgrade, School of Electrical Engineering. Supplied course scaffolding and assets retain their original licensing terms.

## Verification

- Python syntax checks and four command-line regression tests passed.
- `python main.py --help` works without loading desktop dependencies.
- Pygame gameplay and agent correctness have not been tested. Dependency versions remain unpinned until desktop validation establishes a compatible set.
