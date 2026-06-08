"""Startup smoke tests.

These guard the container entrypoint (`python ./main.py`). If `main.py` or the
`SOL` package fail to import, the action container dies on startup before the
worker loop runs, and triggered actions hang until the orchestrator times out
(no clean error surfaces). A fast import check catches that in CI instead.
"""

import importlib


def test_sol_package_reexports_action_classes():
    """The SOL package must expose the action classes that main.py imports."""
    import SOL

    for name in ("SolModule", "CreateDataset", "DeleteDataset", "ExecuteAQuery", "ListQueries"):
        assert hasattr(SOL, name), f"SOL package does not export '{name}'"


def test_main_module_imports():
    """The container entrypoint must import without raising (e.g. ImportError)."""
    main = importlib.import_module("main")
    assert hasattr(main, "SolModule")
