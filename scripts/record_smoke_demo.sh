# Minimal TUI smoke-run recorder → docs/demo_smoke.gif
# Requires: asciinema (pipx/pip) and agg (pipx)
set -euo pipefail

if ! command -v asciinema >/dev/null 2>&1; then
  python -m pip install --user asciinema
fi
if ! command -v agg >/dev/null 2>&1; then
  python -m pip install --user agg
fi

echo "[i] Recording demo.cast (Ctrl-D to stop)…"
asciinema rec demo.cast -c "bash -lc 'printf \"Launching RTAx smoke…\\n\"; sleep 0.5; printf \"Selecting suite: smoke\\n\"; sleep 0.5; printf \"Running…\\n\"; sleep 1; printf \"report written to out/run-123/report/index.md\\n\"; sleep 0.5'"

mkdir -p docs
agg demo.cast docs/demo_smoke.gif --theme dracula --font-size 16 --width 100 --height 30 --speed 1.0
echo "[OK] Wrote docs/demo_smoke.gif"
