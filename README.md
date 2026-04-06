![ソースコードサイズ](https://img.shields.io/github/languages/code-size/yakinoki/code-sandbox-lab)


You can use the following commands to set up a virtual environment and install the necessary packages:

```sh
# Create a virtual environment (optional but recommended)
python -m venv venv

# Activate the virtual environment
# On Windows (Command Prompt)
venv\Scripts\activate
# On Windows (PowerShell)
venv\Scripts\Activate.ps1
# On macOS/Linux
source venv/bin/activate

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

If you encounter an error like:

```vbnet
ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\ci\\argon2-cffi_...'
```

Try installing the problematic package manually with no cache:
```sh
pip install --no-cache-dir argon2-cffi
```

Alternatively, if you're using conda, the following may help:
```sh
conda install -c conda-forge argon2-cffi
```

To exit (deactivate) the virtual environment, simply run:
```sh
deactivate
```

## GitHub Actions

A GitHub Action is configured to run the same `pre-commit` checks automatically on every push and pull request.

The workflow file is located at `.github/workflows/pre-commit.yml`.

No extra setup is required on GitHub; once the repository is pushed, the action will run automatically for:
- `push` to `main` or `master`
- `pull_request` targeting `main` or `master`
