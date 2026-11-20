# RSVP w/ me for your AI

A skill that teaches your AI assistant how to use [RSVP w/ me](https://rsvpw.me). Ask it what's happening this weekend, what you're Going to, what you Liked, what your friends are going to, or who you follow. It answers from your RSVP w/ me account through the RSVP w/ me MCP server, and Likes or un-Likes events when you ask.

The skill is one file: [`skills/rsvp/SKILL.md`](skills/rsvp/SKILL.md).

## You'll need

- A paid RSVP w/ me plan. Connecting an AI is a paid feature. [See paid plans](https://rsvpw.me/upgrade?reason=ai).
- The RSVP w/ me MCP server connected to your AI. The server URL is `https://rsvpw.me/mcp`. When you connect, an rsvpw.me page opens. Sign in there and click Allow. No API key or password to paste.

Your RSVP w/ me settings (Integrations → Connect your AI) have a setup prompt you can paste into your AI, and the skill download.

## Claude (claude.ai and Claude Desktop)

1. Connect the server: in Settings → Connectors, add a custom connector, paste `https://rsvpw.me/mcp`, then sign in.
2. Download [`rsvp-skill.zip`](dist/rsvp-skill.zip) (or get it from your RSVP w/ me settings).
3. Make sure code execution is on (Settings → Capabilities).
4. Go to Customize → Skills, click +, and upload the zip.

## Claude Code

```
/plugin marketplace add turoczy/rsvp-ai-skill
/plugin install rsvpwme@rsvpwme
```

The plugin adds the skill and the RSVP w/ me server. Restart Claude Code, run `/mcp`, pick rsvpwme and sign in. Then ask away, or type `/rsvpwme:rsvp`.

## ChatGPT

1. Connect the server: in Settings → Connectors, add a custom connector, paste `https://rsvpw.me/mcp`, then sign in.
2. Add the skill. Skills work in the ChatGPT desktop app and Codex. Either add this repo as a plugin marketplace:

   ```
   codex plugin marketplace add turoczy/rsvp-ai-skill
   ```

   then install RSVP w/ me from the Plugins Directory. Or unzip [`rsvp-skill.zip`](dist/rsvp-skill.zip) into `~/.agents/skills/`, so the file ends up at `~/.agents/skills/rsvp/SKILL.md`.

## Gemini CLI

```
gemini extensions install https://github.com/turoczy/rsvp-ai-skill
```

The extension adds the skill and the RSVP w/ me server. Then run `/mcp auth rsvpwme` to sign in.

Moved to Antigravity CLI? Google's [migration guide](https://antigravity.google/docs/cli/gcli-migration) says `agy plugin import gemini` converts installed Gemini CLI extensions.

## Building the zip

`dist/rsvp-skill.zip` is built from `skills/rsvp/SKILL.md`:

```
python3 scripts/build_zip.py          # rebuild
python3 scripts/build_zip.py --check  # fail if the zip is out of date
```

The build is deterministic: the same SKILL.md always gives the same zip.

[Privacy](https://rsvpw.me/privacy) · [Terms](https://rsvpw.me/terms)
