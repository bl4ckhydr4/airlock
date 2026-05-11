#!/usr/bin/env bash
set -e
echo "==> Installing Airlock CLI..."
cp airlock /usr/local/bin/airlock
chmod +x /usr/local/bin/airlock
mkdir -p /opt/airlock-api
cp server.py /opt/airlock-api/
cp requirements.txt /opt/airlock-api/
if command -v pip3 &> /dev/null; then
    pip3 install flask flask-cors --break-system-packages 2>/dev/null || pip3 install flask flask-cors
fi
if [ -d /etc/systemd/system ]; then
    cp airlock-api.service /etc/systemd/system/
    systemctl daemon-reload
    systemctl enable airlock-api
    systemctl start airlock-api
    echo "==> API service started on port 5000"
fi
mkdir -p ~/.openclaw/airlock-archives ~/.openclaw/airlock-manifests
echo "==> Airlock installed. Run 'airlock status' to verify."
