# The RSVP w/ me skill

Setup steps for every AI are on the [front page of this repo](../README.md).

The skill is one file: [`skills/rsvp/SKILL.md`](skills/rsvp/SKILL.md). [`dist/rsvp-skill.zip`](dist/rsvp-skill.zip) is the same file packaged for Claude's skill upload.

## Building the zip

`dist/rsvp-skill.zip` is built from `skills/rsvp/SKILL.md`:

```
python3 scripts/build_zip.py          # rebuild
python3 scripts/build_zip.py --check  # fail if the zip is out of date
```

The build is deterministic: the same SKILL.md always gives the same zip.
