# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in Airlock, please report it privately. Do not open a public issue.

Send details including:
- A description of the vulnerability
- Steps to reproduce
- Affected versions or commits
- Any suggested mitigations

We aim to acknowledge reports within **48 hours** and provide an initial assessment within **5 business days**. We will keep you informed of progress and coordinate public disclosure with you.

## Supported Versions

Airlock is currently in early-stage development. Security updates are applied to the `main` branch. Versioned releases with explicit support windows will be introduced in a future release.

## Disclosure Policy

After a fix is released, a security advisory will be published through GitHub's built-in advisory system. Credit will be given to the reporter unless anonymity is requested.

## Security Best Practices for Users

- The Flask API binds to `127.0.0.1` by default. Do not expose it to the public internet without a reverse proxy and HTTPS.
- The `airlock-agent.conf` file is sourced directly by the CLI. Only store trusted commands in this file.
- Review the audit log regularly: `airlock audit`
- Use `airlock force-unseal` only in recovery scenarios — it bypasses integrity verification.
- Keep your workspace archives and manifests in secure, access-controlled directories.
