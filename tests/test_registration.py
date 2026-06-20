"""Smoke tests: the package registers under taskbench.providers."""

from __future__ import annotations

from importlib.metadata import entry_points


def test_planka_entry_point_is_registered() -> None:
    """When the package is installed, the planka adapter must appear under
    the taskbench.providers entry-point group."""
    eps = entry_points(group="taskbench.providers")
    names = {ep.name for ep in eps}
    assert "planka" in names, f"expected 'planka' among {names}"


def test_planka_entry_point_loads_provider_class() -> None:
    """Loading the entry point yields a callable PlankaProvider class."""
    eps = entry_points(group="taskbench.providers")
    ep = next(ep for ep in eps if ep.name == "planka")
    cls = ep.load()
    # Sanity: it has the protocol's lifecycle methods.
    assert hasattr(cls, "__aenter__")
    assert hasattr(cls, "__aexit__")
    assert hasattr(cls, "get_user")
    assert hasattr(cls, "get_tasks")
