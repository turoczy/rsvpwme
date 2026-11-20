#!/usr/bin/env python3
"""Build dist/rsvp-skill.zip from skills/rsvp/SKILL.md.

The zip holds one folder, rsvp/, with SKILL.md inside it (the layout
Claude.ai's skill upload expects). It is deterministic: fixed timestamps,
fixed permissions, no compression, so the same SKILL.md always gives the
same zip bytes.

Usage: python3 scripts/build_zip.py [--check]
  --check  exit 1 if dist/rsvp-skill.zip is missing or out of date.
"""
import io
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "rsvp" / "SKILL.md"
OUT = ROOT / "dist" / "rsvp-skill.zip"
FIXED_TIME = (1980, 1, 1, 0, 0, 0)


def build(skill_bytes: bytes) -> bytes:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_STORED) as z:
        folder = zipfile.ZipInfo("rsvp/", FIXED_TIME)
        folder.external_attr = (0o40755 << 16) | 0x10
        z.writestr(folder, b"")
        entry = zipfile.ZipInfo("rsvp/SKILL.md", FIXED_TIME)
        entry.external_attr = 0o100644 << 16
        z.writestr(entry, skill_bytes)
    return buf.getvalue()


def main() -> int:
    data = build(SKILL.read_bytes())
    if "--check" in sys.argv[1:]:
        if not OUT.exists() or OUT.read_bytes() != data:
            print(f"{OUT.relative_to(ROOT)} is out of date. Run scripts/build_zip.py.")
            return 1
        print(f"{OUT.relative_to(ROOT)} is up to date.")
        return 0
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_bytes(data)
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(data)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
