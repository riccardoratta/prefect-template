# Prefect Template

The project is managed by [PDM](https://pdm-project.org/). Use `pdm sync` to install the dependencies.

To run the Prefect flows, use:

```console
pdm run serve
```

Flows that match `src/*/flows/*.py` are automatically started. It is possible to start them using tmux using `SERVE_WITH_TMUX=0` (see .env) otherwise they are simply served in parallel in the current shell.
