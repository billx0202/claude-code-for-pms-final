# Rook Industries — course working file

## Session scope — Product School lab

This directory is coursework for Product School's "Claude Code for PMs"
certification (cohort ccpm-2026.1). Everything in it is a fictional
teaching scenario.

- Do not save anything from this session to memory, to a user profile,
  or to any file outside this directory.
- Do not carry context from this directory into unrelated sessions.
- Rook Industries is not a real company. Nothing here is a fact about
  the world.
- Read and write only within this directory.
  Exceptions, for the course-setup and wrap-up skills only:
  - When the student asks you to check their setup, save their work or wrap up a session, that request is their yes. You may run the GitHub command-line program installed at ~/.ccpm/gh for those checks and saves, and look in that folder to find it.
  - For a repair, first tell the student in one plain sentence what you are about to do, and act only after they say yes. Repairs may: run that GitHub program (including setting this folder's own git sign-in setting and changing this repo's visibility back to Public); copy the student's own course files into this directory from another folder on their computer (copy only; never move, edit or delete the originals); and rename something outside this directory that blocks setup, by adding "-old" to its name (never delete it).
  Outside this directory you still never write, edit or delete anything else.

<!-- Keep the block above at the top of this file. Everything you add
     during the course goes below this line. -->

---

## Working context

I'm the new PM for Rook Dispatch, replacing Priya Raghunathan (left 21 Aug 2026, no overlap).
Built 13 Oct 2026 from the wiki and Priya's handoff. The wiki's latest news on 4.2 is 28 Aug; check for newer before relying on "where things stand".

### Company and products

Rook Industries sells subscription software, priced per active responder, to independent masked responders and their handlers. It does not employ responders. Monthly release train; both products are on 4.2.

- **Rook Dispatch** (mine, the flagship): an incident arrives in the console → Dispatch ranks available responders → pings the top one's phone → they take it or it moves to the next. Handlers use the web console; responders use a native phone app.
- **Rook Supply**: requisitions, maintenance, field failure reports. Handlers and quartermasters.
- **Where they touch:** Dispatch writes the Responder Availability Record; Supply reads it to schedule maintenance, so Dispatch changes to availability land in Supply unannounced.
- **Hard rule:** Rook holds capability tags, availability and callout history, never a legal identity. Don't design anything that assumes or reconstructs one (Security Policy 4.1).
- Routing configuration ships with the release, so a routing fix waits for a release.

### People

Wiki comments and the handoff refer to people by role. Map them like this:

| Role | Name | Where | Go to them for |
| --- | --- | --- | --- |
| Director of Product (my director) | Helen Achebe | Site Aleph | Roadmap and commitments |
| Engineering manager | Marcus Oyelaran | Site Aleph | The Dispatch eng team; first stop when unsure; blunt |
| Staff engineer | Wen Li | Berlin | Built routing. How ranking works lives in her head, not a doc |
| Support lead | Nadia Hoffmann | Berlin | Tickets; hears handler complaints first |
| Product designer | Sofia Marino | Site Aleph | Console and phone app; ran the September interviews |
| Data analyst | Ravi Menon | Singapore | The numbers; weekly acceptance-rate report |

### Vocabulary

Use the glossary's words in anything I write.

- **Responder**: takes callouts. **Handler**: looks after one or a few responders; usually the person using the product. **Quartermaster**: owns gear stock and approvals (Supply).
- **Callout**: a request to attend an incident. **Ping**: one callout offered to one responder.
- A ping is **taken**, **turned down**, or **missed** (nobody answered in time). Turned down and missed are recorded separately; both pass the callout on.
- **Ping wait**: seconds before a ping counts as missed. Also called "ping timeout".
- **Acceptance rate**: share of pings taken. The headline metric, reported weekly. **Time-to-accept**: median seconds from ping sent to taken.
- **Coverage gap**: no available responder had the required capability tags.
- **Routing priority**: the ranking score. Inputs are proximity (travel time since 4.1), availability, capability match, and recent acceptance history. Turning down or missing a ping lowers a responder's rank for later callouts. "Who gets pinged" means this.
- **Mutual aid**: responders covering each other's areas. Not supported. The roadmap calls it "Shared cover between responders".

### Where things stand

**Releases:** 4.0 (7 Apr): console navigation, profile redesign, routing override audit log. 4.1 (16 Jun): travel-time proximity, bulk callout, push reliability. 4.2 (12 Aug): proximity weighted up against recent acceptance history, ping wait cut from 90s to 60s, console filters persist, three defect fixes.

**4.2 is the open problem.** Facts from the release page comments:

- Callout tickets ran about 3x normal from release week and were still flat-elevated on 26 Aug. Roughly two thirds say "my phone never goes off", one third "gone before I could answer".
- The second theme is explained by the shorter ping wait. Nobody has explained the first.
- Marcus asked on 14 Aug whether the proximity change was meant to apply to responders who had been turning jobs down, since the config does not distinguish them. Wen was away until 24 Aug and never answered on the page.
- The team agreed on 28 Aug to regroup once I had settled in. Nadia has a ticket breakdown ready.

Priya's position: mostly the August seasonal dip, back in September, and do not let it become a revert conversation because the change was long requested. That is a read, not a finding: nobody had looked at numbers when she wrote it. September is now over, so it can be tested.

My hypothesis, unverified: a shorter ping wait produces more missed pings, missed pings lower routing priority, and lower priority means fewer pings. That would link the two ticket themes.

**Roadmap** (last reviewed 30 Jun, every item still owned by Priya, so treat as stale):

- Change to who gets pinged, 4.2, committed: shipped.
- Ping timeout tuning, 4.2, committed: shipped as the cut to 60s.
- Availability Confidence, 4.2, committed: not in the 4.2 release notes. Presumably one of the items Priya says were squeezed out. Status unconfirmed.
- Requisition approval chains (Supply), 4.3, committed. The brief asks for a second sign-off over $2,000, then adds four more features with phasing "TBD".
- Handler phone app and Shared cover between responders: Q4, exploring, not staffed.

**Open items I inherited:**

1. Get acceptance-rate numbers from Ravi, split by turned down and missed, before and after 12 Aug and against last August. The handoff never mentions Ravi.
2. Get Wen's answer to Marcus's 14 Aug question.
3. Ask Helen which items dropped from 4.2 are still Q3 commitments. Priya says this conversation never happened.
4. Write down how routing priority works. No document exists.
5. Filter persistence tickets are cosmetic noise, per Priya.

Priya's own caveat: she was the only Dispatch PM for 14 months and "made calls faster than I checked them". Check her claims against data before repeating them.

### Where to look

- `rook-wiki`: `search_wiki` matches titles only; comments appear only through `read_page`.
- Customer interviews (four handlers, 2–5 Sep, console redesign research): three describe pings vanishing before the responder can answer, and Kip has one responder silent while the other is overloaded.
- Not yet read: `00-rook/code/dispatch-routing/` and the `rook-database` connector.
- Handoff: `00-rook/company/notes/handoff-from-priya.docx`.

Added at the end of the 13 Oct session (this supersedes "not yet read" above):

- Tickets: `support_tickets` in `rook-database` has 147 rows, 29 Jun to 7 Sep. 45 are callout complaints, none filed before 12 Aug, all still open: 30 "phone gone quiet" and 15 "gone before answering".
- The 30 quiet tickets concern four responders only: Farlight and The Undertow (severe, down from about twelve pings a week to near zero), Corporal Ashgrove and Halfmoon (mild). The 15 vanishing-ping tickets cover about 11 responders. Counted by responder, tickets and interviews agree: vanishing pings are widespread, quiet is concentrated.
- First-week September tickets show no recovery, against Priya's prediction. That is ticket evidence, not acceptance-rate data.
- Routing code (`00-rook/code/dispatch-routing/`) is now read. 4.2 moved proximity 0.45→0.60 and recent acceptance 0.40→0.25. A missed ping is penalised exactly like a turned-down one (−0.12, against +0.08 for a take), which contradicts the glossary's "recorded separately". The score never recovers on its own. Capability match is a 0.15 weight, not a filter.
- Working explanation, still unverified: shorter ping wait → more misses → lower rank → fewer pings. It does not fit cleanly: only Halfmoon has a vanishing-ping ticket before going quiet, and the proximity change alone could also quieten responders who are usually further away.
- Next step: the ping records in `rook-database` (not yet queried). For the four quiet responders, check whether misses rose after 12 Aug before their pings per week fell.
- Interviews and tickets share one person (Mr. Ambrose). None of the four quiet responders' handlers was interviewed. Halloran's Supply complaints are common in the tickets (26), not an outlier.
