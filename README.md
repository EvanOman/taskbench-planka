# taskbench-planka

Planka adapter for [Taskbench](https://github.com/EvanOman/taskbench) — a backend-pluggable, agent-first task CLI.

Implements the `TaskProvider` protocol from `taskbench.core` against [Planka](https://planka.app/)'s Kanban API (via [plankapy](https://github.com/Robert-Nogueira/plankapy)).

## Concept mapping

| TaskProvider concept | Planka concept |
|---|---|
| Workspace / Team | synthetic singleton derived from the logged-in user |
| Space | Project |
| Folder | no-op (returns empty / synthetic placeholder) |
| List | Board |
| Status | List (column within a Board) |
| Task | Card |
| Comment | Comment (Action) |

## Install

```bash
# Once published, alongside taskbench:
uv tool install taskbench
uv pip install taskbench-planka --with taskbench

# Or for development (taskbench from git):
uv pip install git+https://github.com/EvanOman/taskbench-planka.git
```

## Configure

Set the standard Planka env vars:

```bash
export TASKBENCH_PROVIDER=planka
export PLANKA_URL=http://localhost:1337    # or your Railway URL
export PLANKA_USERNAME=admin               # or PLANKA_EMAIL
export PLANKA_PASSWORD=...
```

Then any `taskbench ...` command routes through the Planka adapter:

```bash
taskbench workspace list
taskbench discover hierarchy
taskbench task list --list-id <board-id>
```

## Discovery

This package registers itself under the `taskbench.providers` entry point group with the name `planka`. Taskbench's factory at `taskbench.core.providers.get_provider()` discovers it via `importlib.metadata` — no code changes are needed in Taskbench itself. To add a new backend, follow the same pattern (one adapter module, one entry point).

## Status

This adapter targets Planka v2 API and was the reference implementation while Taskbench was still `clickup-toolkit`. It is functional but light on automated tests; the smoke path is exercised against a [planka-deploy](https://github.com/EvanOman/planka-deploy) instance (private repo: Railway compose + seed).

## License

MIT, matching Taskbench.
