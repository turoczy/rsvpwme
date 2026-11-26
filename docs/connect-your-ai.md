# Connect your AI

You can connect an AI assistant like Claude or ChatGPT to RSVP w/ me, then just ask it things. "What's happening in Portland this weekend?" "Find me a free meetup next week."

It connects through what's called an MCP server, a standard way for AI apps to plug into other services. Ours lives at `https://rsvpw.me/mcp`. You don't need an API key or a password. When you connect, an rsvpw.me page opens. Sign in there with Google and click **Allow**.

**Setup steps for each app** (Claude, ChatGPT, Claude Code, Gemini CLI) are on the [front page of this repo](../README.md). Your Settings page also has the address and a copy button: Settings → Integrations → **Connect your AI**.

Look for the **Pro tip** cards on the River, event pages and My events. Until you've connected an AI, the card has a short message you can copy and paste into it to get set up, plus a button to connect. Once you're connected, it first offers a message that installs the RSVP w/ me skill, then a different question to ask your AI each time you visit. Click **Copy** to grab just the text in the box. On an event page it includes the event's name and link. Close any card with ×.

## What it can do

**Free:** connecting is free. Your AI can search events, look up an event and browse the tags.

**Paid:** it can also see your plans and friends, and Like events for you. That means:

- Events you've Liked or are Going to, and your past events
- Who you follow (people and tags)
- Which friends are going, for any dates you name ("Is my friend Stephen going to anything on Friday?")
- Which friends you most often say you're Going to the same events with
- Your Inbox: invites, follow requests, notifications and introductions from friends who think you should meet someone (it can read them, not send them)
- Like and un-Like events for you. The Allow page says so when the app asks for it. We tell your AI to Like only when you ask.

It can't change anything else.

On a free account, if you ask for something that needs the paid plan, your AI gets a short note saying so and keeps helping with search. The note has your own link to the paid plan (a one-time price, no subscription). It works for 30 minutes and goes straight to checkout, with no sign-in. When you've paid, the page says you're all set. If your AI still says "paid plan," start a new chat.

## Things to ask

Ask the way you'd ask a friend. A few to start with:

**Anyone (free):**

- "What's happening in Portland this weekend?"
- "Find me a free meetup next week."
- "What's the most popular event this week?"
- "Any AI or startup events in Seattle next month?"
- "What kinds of events can you search for?"
- "Tell me about this event: https://rsvpw.me/events/…" (paste any event link)

**Paid:**

- "What am I up to this weekend?"
- "What did I Like that's coming up?"
- "Are any of my friends going to something this week?"
- "Is my friend Stephen going to anything on Friday?"
- "Two things Thursday night. Which one has more of my friends going?" (close friends count first)
- "Who do I go to events with most?"
- "What kinds of events do I usually go to?"
- "Find me upcoming events like the ones I usually go to."
- "Anything in my Inbox I need to answer?"
- "Who am I following?"
- "Like the first two." (after a search, so it knows which ones)

## The Allow page

When you connect, you see what the app is asking for, and where you'll be sent after. If you don't recognize that address, don't allow this. Some apps say **Unverified app**. That means RSVP w/ me hasn't checked who made it.

Click **Deny** and nothing is shared.

## How many apps

- **Free:** keep 2 AI apps connected at once, and connect up to 2 new ones an hour and 3 a day. Reconnecting an app you already have doesn't count. Connecting a third disconnects one, and the Allow page tells you which.
- **Paid:** keep up to 25 connected at once.

## When you connect a new app

We email you. The subject starts "A new app", for example "A new app can see your RSVP w/ me account". If that wasn't you, the email has a link to disconnect it.

## Seeing and disconnecting

Settings → Integrations → **Connect your AI** lists every connection: its name, what it can do, when it was created and last used. Click **Revoke** to disconnect one, and it stops working. There's also a list of recent agent activity: what your AI changed (like a Like) and any time it hit a limit. Activity older than 30 days is deleted.

Paid accounts can also make up to 5 **tokens for other apps** in the same spot.

## Send an event to your AI

On any event, click **Invite**, then **Send to my agent**. It copies the event so you can paste it to your AI.

## Want it to know RSVP w/ me better?

There's a skill file that teaches your AI how to use RSVP w/ me well. It's in this repo too. The [front page](../README.md) says how to add it.
