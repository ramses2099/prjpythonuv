# prjpythonuv
Project example using uv package manager

# Install uv package manager
pip install uv

# Init project
```
$ uv init [PROJECT_NAME]
Initialized project `[PROJECT_NAME]` at `/home/user/[PROJECT_NAME]`

# Install package
$ cd [PROJECT_NAME]

$ uv add ruff
Creating virtual environment at: .venv
Resolved 2 packages in 170ms
   Built [PROJECT_NAME] @ file:///home/user/[PROJECT_NAME]
Prepared 2 packages in 627ms
Installed 2 packages in 1ms
 + [PROJECT_NAME]==0.1.0 (from file:///home/user/example)
 + ruff==0.5.5

$ uv run ruff check
All checks passed!

```
# Install Pytest
uv add --dev pytest
```
$ uv run pytest
```

