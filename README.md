# RSVP w/ me for your AI

Connect your AI assistant to [RSVP w/ me](https://rsvpw.me). Ask it what's happening this weekend, what you're Going to, what you Liked, what your friends are going to, or who you follow. It answers from your RSVP w/ me account, and Likes or un-Likes events when you ask.

There are two pieces:

- **The MCP server** at `https://rsvpw.me/mcp`. This is the connection to your account. When you connect, an rsvpw.me page opens. Sign in there and click Allow. No API key or password to paste.
- **The skill**, one file ([`rsvp-skill/skills/rsvp/SKILL.md`](rsvp-skill/skills/rsvp/SKILL.md)) that teaches your AI how to use the server well.

Connecting your AI to search events is free. Your plans, friends, Inbox and Liking need the paid plan. [See what the paid plan adds](https://rsvpw.me/upgrade?reason=ai).

Your RSVP w/ me settings (Integrations → Connect your AI) also have a setup prompt you can paste into your AI.

## Claude Code

```
/plugin marketplace add turoczy/rsvpwme
/plugin install rsvpwme@rsvpwme
```

The plugin adds the skill and the server. Restart Claude Code, run `/mcp`, pick rsvpwme and sign in. Then ask away, or type `/rsvpwme:rsvp`.

## Claude (claude.ai and Claude Desktop)

1. Connect the server: in Settings → Connectors, add a custom connector, paste `https://rsvpw.me/mcp`, then sign in.
2. Download [`rsvp-skill.zip`](rsvp-skill/dist/rsvp-skill.zip).
3. Make sure code execution is on (Settings → Capabilities).
4. Go to Customize → Skills, click +, and upload the zip.

## ChatGPT

1. Connect the server: in Settings → Connectors, add a custom connector, paste `https://rsvpw.me/mcp`, then sign in.
2. Add the skill. Skills work in the ChatGPT desktop app and Codex. Either add this repo as a plugin marketplace:

   ```
   codex plugin marketplace add turoczy/rsvpwme
   ```

   then install RSVP w/ me from the Plugins Directory. Or unzip [`rsvp-skill.zip`](rsvp-skill/dist/rsvp-skill.zip) into `~/.agents/skills/`, so the file ends up at `~/.agents/skills/rsvp/SKILL.md`.

## Gemini CLI

```
gemini extensions install https://github.com/turoczy/rsvpwme
```

The extension adds the skill and the server. Then run `/mcp auth rsvpwme` to sign in.

Moved to Antigravity CLI? Google's [migration guide](https://antigravity.google/docs/cli/gcli-migration) says `agy plugin import gemini` converts installed Gemini CLI extensions.

## Help

Questions, or trouble connecting? Email [rick@piepdx.com](mailto:rick@piepdx.com).

[Privacy](https://rsvpw.me/privacy) · [Terms](https://rsvpw.me/terms)
