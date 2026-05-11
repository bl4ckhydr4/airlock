#!/usr/bin/env python3
"""
Airlock API — Flask wrapper around the airlock CLI.
Listens on localhost:5000. Frontend calls this, never the CLI directly.
"""

import subprocess
import json
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

AIRLOCK_BIN = "/usr/local/bin/airlock"

def run_airlock(args, stdin_data=None):
    try:
        result = subprocess.run(
            [AIRLOCK_BIN] + args,
            capture_output=True,
            text=True,
            timeout=30,
            input=stdin_data
        )
        if result.returncode != 0:
            try:
                return json.loads(result.stdout or result.stderr), result.returncode
            except json.JSONDecodeError:
                return {"error": "CLI_ERROR", "message": result.stderr or result.stdout}, 500
        return json.loads(result.stdout), 200
    except subprocess.TimeoutExpired:
        return {"error": "TIMEOUT", "message": "Airlock command timed out."}, 504
    except FileNotFoundError:
        return {"error": "AIRLOCK_NOT_FOUND", "message": f"Airlock binary not found at {AIRLOCK_BIN}."}, 500
    except Exception as e:
        return {"error": "INTERNAL_ERROR", "message": str(e)}, 500

# ─── Workspace endpoints ──────────────────────────────────────

@app.route("/api/airlock/status", methods=["GET"])
def get_status():
    data, code = run_airlock(["status"])
    return jsonify(data), code

@app.route("/api/airlock/seal", methods=["POST"])
def seal():
    data, code = run_airlock(["seal"])
    return jsonify(data), code

@app.route("/api/airlock/unseal", methods=["POST"])
def unseal():
    body = request.get_json(silent=True) or {}
    workspace = body.get("workspace", "")
    if not workspace:
        return jsonify({"unsealed": False, "error": "MISSING_WORKSPACE", "message": "No workspace specified."}), 400
    data, code = run_airlock(["unseal", workspace])
    return jsonify(data), code

@app.route("/api/airlock/force-unseal", methods=["POST"])
def force_unseal():
    body = request.get_json(silent=True) or {}
    workspace = body.get("workspace", "")
    if not workspace:
        return jsonify({"unsealed": False, "error": "MISSING_WORKSPACE", "message": "No workspace specified."}), 400
    data, code = run_airlock(["force-unseal", workspace])
    return jsonify(data), code

@app.route("/api/airlock/settings", methods=["GET"])
def get_settings():
    data, code = run_airlock(["settings"])
    return jsonify(data), code

@app.route("/api/airlock/settings", methods=["POST"])
def save_settings():
    body = request.get_json(silent=True) or {}
    data, code = run_airlock(["save-settings"], stdin_data=json.dumps(body))
    return jsonify(data), code

@app.route("/api/airlock/audit", methods=["GET"])
def get_audit():
    data, code = run_airlock(["audit"])
    return jsonify(data), code

@app.route("/api/airlock/workspaces", methods=["GET"])
def get_workspaces():
    data, code = run_airlock(["workspaces"])
    return jsonify(data), code

@app.route("/api/airlock/create", methods=["POST"])
def create_workspace():
    body = request.get_json(silent=True) or {}
    name = body.get("name", body.get("key", ""))
    if not name:
        return jsonify({"created": False, "error": "MISSING_NAME", "message": "No workspace name specified."}), 400
    data, code = run_airlock(["create", name])
    return jsonify(data), code

@app.route("/api/airlock/delete", methods=["POST"])
def delete_workspace():
    body = request.get_json(silent=True) or {}
    workspace = body.get("workspace", "")
    if not workspace:
        return jsonify({"deleted": False, "error": "MISSING_WORKSPACE", "message": "No workspace specified."}), 400
    data, code = run_airlock(["delete", workspace])
    return jsonify(data), code

# ─── Agent lifecycle endpoints ────────────────────────────────

@app.route("/api/airlock/agent/status", methods=["GET"])
def agent_status():
    data, code = run_airlock(["agent-status"])
    return jsonify(data), code

@app.route("/api/airlock/agent/stop", methods=["POST"])
def agent_stop():
    data, code = run_airlock(["agent-stop"])
    return jsonify(data), code

@app.route("/api/airlock/agent/start", methods=["POST"])
def agent_start():
    data, code = run_airlock(["agent-start"])
    return jsonify(data), code

# ─── Health ───────────────────────────────────────────────────

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("AIRLOCK_API_PORT", 5000))
    app.run(host="127.0.0.1", port=port, debug=False)