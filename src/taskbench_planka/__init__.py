"""Planka adapter for the Taskbench CLI.

Registered as an entry point under ``taskbench.providers`` with the name
``planka``. With this package installed, set ``TASKBENCH_PROVIDER=planka``
and Taskbench's factory will load this adapter.
"""

from .provider import PlankaProvider

__all__ = ["PlankaProvider"]
__version__ = "1.0.0"
