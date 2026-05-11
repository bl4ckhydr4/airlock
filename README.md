# Airlock

**Seal, verify, and switch between AI agent workspaces with cryptographic integrity.**

Airlock is a command-line tool (with an optional web dashboard) that safely switches between multiple AI agent identities. Built for multi-agent pipelines but works with any workspace-based agent.

## Why Airlock?

- **Cryptographic integrity**: SHA‑256 hashing on seal, verified on load.
- **Safe isolation**: Double‑door airlock — no two workspaces active at once.
- **Git integration**: Auto‑commit and auto‑push optional.
- **Agent lifecycle hooks**: Auto‑stop/start your agent during switches.
- **Audit trail**: Every seal, unseal, and forced load is logged.
- **Works anywhere**: CLI on any Linux machine; optional web dashboard.

## Quick Start

```bash
git clone https://github.com/bl4ckhydr4/airlock.git
cd airlock
chmod +x install.sh
sudo ./install.sh
cat > README.md << 'ENDOFREADME'
# Airlock

**Seal, verify, and switch between AI agent workspaces with cryptographic integrity.**

Airlock is a command-line tool (with an optional web dashboard) that safely switches between multiple AI agent identities. Built for multi-agent pipelines but works with any workspace-based agent.

## Why Airlock?

- **Cryptographic integrity**: SHA‑256 hashing on seal, verified on load.
- **Safe isolation**: Double‑door airlock — no two workspaces active at once.
- **Git integration**: Auto‑commit and auto‑push optional.
- **Agent lifecycle hooks**: Auto‑stop/start your agent during switches.
- **Audit trail**: Every seal, unseal, and forced load is logged.
- **Works anywhere**: CLI on any Linux machine; optional web dashboard.

## Quick Start

```bash
git clone https://github.com/bl4ckhydr4/airlock.git
cd airlock
chmod +x install.sh
sudo ./install.sh

