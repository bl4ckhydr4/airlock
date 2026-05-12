## Contributing

## Code of Conduct

This project follows the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).
By participating, you agree to uphold this code. Please report unacceptable behavior to the project maintainer.

Contributions are welcome, especially around reliability, packaging, documentation, testing, and dashboard integration.

Recommended local checks before opening a pull request:

```bash
bash -n airlock
bash -n install.sh
python3 -m py_compile server.py
```

Optional linting:

```bash
shellcheck airlock install.sh
```

Suggested contribution workflow:

```bash
git clone https://github.com/bl4ckhydr4/airlock.git
cd airlock
git checkout -b improve-airlock
```

Make your changes, test the CLI locally, then open a pull request with:

* What changed
* Why it changed
* How it was tested
* Any migration or compatibility notes

Good first contribution areas:

* Add `docs/assets` visuals
* Add a GitHub Actions workflow
* Add API endpoint tests
* Improve installation safety checks
* Expand workspace discovery behavior
* Add examples for common agent runtimes

Do not include private workspace memory, secrets, tokens, or sensitive agent configuration in public issues.

### Suggesting Features

Open a GitHub Issue with:
- What problem the feature solves
- How you'd expect it to work
- Any alternatives you've considered

### Pull Requests

1. Fork the repository
2. Create a branch: `git checkout -b improve-airlock`
3. Make your changes
4. Verify the CLI is still valid:
   ```bash
   bash -n airlock
   bash -n install.sh
   python3 -m py_compile server.py
   ```
