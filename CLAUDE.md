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

Added at the end of the 14 Oct session, from the `pings` table. This corrects the lines above: the "four quiet responders" were wrong, and the explanation is now confirmed by data.

- `pings` has 1,696 rows, 29 Jun to 6 Sep, and passed basic data checks. Missed pings went from 2.3% to 18% on release day, and taken from 77% to 64%. The gap after a missed ping is 91–93 seconds before the release and 61–63 after, so the 60-second wait was live from day one.
- The four responders who were shut out are Farlight, The Undertow, Meteor Mite and Vesper. Each fell from about 12 pings a week to 3 or 4, with 53–64% of the rest missed. Corporal Ashgrove and Halfmoon fell only about 20%. The handlers of Vesper (Aunt Dot) and Meteor Mite (Kip) filed no tickets.
- Mechanism, confirmed in the data: all 16 responders missed more, but the four's misses clustered on 12–14 Aug. Replaying the scores with the miss penalty predicts who is skipped in their own area (pinged first 13% of the time below a score of 0.4, against 72–80% above). Without the penalty, the replay can't explain it. Proximity is not the cause, and the four were not weaker responders beforehand. Neighbours took the work: The Gale +42%, Sgt. Falkirk +40%.
- Farlight had no pings from 28 Aug to the end of the data on 6 Sep, while 16 Uptown callouts went to Sgt. Falkirk, Cindermark and Sgt. Bulwark. Callouts almost never go past the third ping. Ticket counts match the pings exactly but arrive 3–5 days later; only about 1 miss in 7 was ever reported.
- The season was somewhat quieter: callouts fell from about 141 a week to about 114 after the release, and overnight callouts halved. That explains some volume, not the misses. There is no previous-year data to test "August is always soft".
- Open questions: are the misses slow answers or late notifications (the 4.2 notification fix)? Also availability records, handler overrides (most unfilled callouts stop after one ping), real production scores, and data since 6 Sep. Recommendation drafted: reset the four's scores, stop penalising a miss like a turn-down or let scores recover, then decide the ping wait. Confirm with Wen and Marcus first.

Added at the end of the 16 Oct session (Module 5, Helen's request in `05-super-speed/director-request.txt`):

- Helen asked for a one-pager plus something clickable, seen from the person it happens to ("not a setting"), before anyone touches the code. Wen's 2019 TODO in `history.py` asks whether scores should ease back to neutral on their own; nobody answered it until now.
- The brief is `05-super-speed/brief.md`, "Missed isn't No". It covers four changes: score a miss as its own, smaller penalty; let scores recover toward neutral; explain the drop on the handler's coverage card and on the responder's phone; reset the four to their pre-12 Aug scores. It does not change the ping wait, revert proximity, touch the Responder Availability Record, or name other responders. It also has a "Who benefits" section and an eight-row risks table.
- The prototype is `05-super-speed/prototype.html`. It replays Meteor Mite's real weeks (27 Jul – 5 Sep) in Kip's console and on her phone, with a "Today (4.2)" vs "With the fix" toggle. A styled version of the brief is in `brief-missed-is-not-no.html`.
- Meteor Mite (she/her) and The Gale are both Kip's, both in Eastgate (`responders` table; the `callouts` table has area). Meteor Mite's pings by week: 12, 11, 10, 4, 2, 1. She was offered first on 5–7 Eastgate callouts a week before 4.2, then 2, 1 and 0. The Gale took 16 of 17 Eastgate callouts in the week of 31 Aug. Her first misses were 13:43 and 15:12 on 13 Aug and 07:26 on 14 Aug, all daytime.
- Biggest open risks: being too soft on misses, if someone who has really stopped taking work keeps getting pinged; and whether the misses are late notifications rather than slow answers. The catch-up reset also needs real production scores from Wen, because ours come from a replay. Helen still has to decide whether this goes as a release exception or on the next train.
