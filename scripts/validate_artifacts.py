"""
Validate examples/events.jsonl and examples/metrics.json against docs/schema/* using jsonschema.

Usage:
  python scripts/validate_artifacts.py
"""
import json, sys, pathlib
from jsonschema import validate, Draft7Validator

ROOT = pathlib.Path(__file__).resolve().parents[1]
schemas = ROOT / "docs" / "schema"
events_schema = json.loads((schemas / "events.schema.json").read_text(encoding="utf-8"))
metrics_schema = json.loads((schemas / "metrics.schema.json").read_text(encoding="utf-8"))

# Validate metrics.json
metrics = json.loads((ROOT / "examples" / "metrics.json").read_text(encoding="utf-8"))
Draft7Validator(metrics_schema).validate(metrics)
print("[OK] metrics.json validates")

# Validate events.jsonl (each line)
errors = 0
for i, line in enumerate((ROOT / "examples" / "events.jsonl").read_text(encoding="utf-8").splitlines(), 1):
    if not line.strip():
        continue
    obj = json.loads(line)
    try:
        Draft7Validator(events_schema).validate(obj)
    except Exception as e:
        print(f"[ERR] events line {i}: {e}")
        errors += 1

if errors:
    sys.exit(1)
print("[OK] events.jsonl validates")
