# Missed isn't No

One-pager · Product, Dispatch · 16 October 2026 · For Helen Achebe

## Problem
Since 4.2 (12 Aug), a ping waits 60 seconds instead of 90. Missed pings went from 2.3% to 18% overnight. Routing priority scores a **missed** ping exactly like a **turned down** one (−0.12, while a take earns back +0.08), and the score never recovers by itself. A responder who misses a few pings drops in the order, so they get fewer pings, which means fewer chances to take one and climb back. Four responders fell into that loop: Farlight, The Undertow, Meteor Mite and Vesper. Each went from about 12 pings a week to 3 or 4. Farlight got none at all from 28 Aug onward, while 16 Uptown callouts went to neighbours. Nobody could see it happening. Two of the four handlers never filed a ticket.

The glossary already says missed is "recorded separately from turned down". The code doesn't do that. Wen Li's 2019 note beside it asks whether a score should "ease back" on its own, and nobody answered.

## Who it's for
**Kip**, handler for Meteor Mite and The Gale. On 4 Sep Kip told Sofia Marino that the two coverage cards "might as well be two different products". Mite is dead quiet and texting to ask if something's broken. The Gale is exhausted (+42% pings). Kip's answer to Mite was "hang in there", because the console gave Kip nothing better.

**Meteor Mite**, the responder who went quiet. Farlight is the most severe case, and the one we traced ping by ping in the data. We're designing for Mite because Mite's handler is on record. The same design covers Farlight.

## What changes for them

**1. A missed ping stops counting as a no.** A miss gets recorded and scored as its own outcome, with a much smaller penalty than a turn-down. Scores also ease back toward neutral over a few weeks, which answers Wen's 2019 question with a yes. Someone who had a bad week of thumbs-on-a-gone-screen isn't still paying for it in October.

**2. Kip's coverage card says why it's quiet.** When a responder's pings drop well below their usual week, the card shows one plain line in Rook's words:
> *Meteor Mite — 3 pings this week (usually ~12). 9 of the last 14 were missed, not turned down. Mite is being offered later in the order in their area.*

The line links to that responder's recent pings: taken / turned down / missed, with the time of each. Kip can now tell Mite something true, like "you're not forgotten, you're missing them, check your notifications", instead of "hang in there". It also explains the other card: The Gale is busy *because* Mite is quiet.

**3. Kip gets an alert after two days in a row with no pings.** If Meteor Mite gets no pings for two days running, while Eastgate had callouts she could have been offered, Kip's console flags it:
> *Tue 25 Aug: no pings for Meteor Mite for 3 days in a row (since Sun 23 Aug), while 7 Eastgate callouts went out.*

Her card also shows her pings day by day, so the quiet days stand out. We recommend two days, not one. In her real data, a one-day rule would have fired three times in the two normal weeks before 4.2 (29 Jul, 31 Jul, 9 Aug), when The Gale simply got there first. The two-day rule never fires before 4.2, and from 24 Aug it catches every stretch of two or more quiet days. It is a fixed rule, not a setting.

**4. Mite's phone tells Mite what happened.** After a missed ping, the app says: *"You missed a ping at 23:14. It went to another responder. Missed pings don't count against you the way turning one down does."* If several misses land close together, it adds: *"Several pings missed recently. Check that notifications are on for Rook."* Silence no longer means "something's broken" or "they've dropped me".

**5. One-time catch-up for the four.** At launch, the four affected responders go back to where their scores stood before 12 Aug, so they don't have to earn their way out of a hole we dug.

## What it deliberately doesn't do
- **Doesn't change the ping wait.** 60 vs 90 seconds is a separate decision, made after this lands and Ravi Menon's numbers show what's left.
- **Doesn't revert the proximity change.** The data shows proximity isn't the cause, and it was long requested. This is not a 4.2 revert.
- **Isn't a setting or a knob.** Handlers don't tune penalties. Nobody sees a raw routing-priority number, and responders never see a rank or a leaderboard.
- **Doesn't name who took the callout** on the responder's phone. It just says "another responder".
- **Doesn't touch the Responder Availability Record**, so nothing lands in Supply unannounced.
- **Doesn't assume or reconstruct anyone's legal identity** (Security Policy 4.1). It uses callout history only.
- **Doesn't fix late notifications.** If some misses turn out to be delivery delays rather than slow thumbs, that's a separate fix. The "check notifications" nudge only points to it.
- **Isn't Availability Confidence, Shared cover between responders, dark mode or per-responder alert sounds.** All of those are real asks, and all are out of scope here.

## Who benefits
- **Most:** the four who were shut out and their handlers, Kip and Aunt Dot, plus Farlight's and The Undertow's handlers, whom we haven't spoken to.
- **Some:** all 16 responders. Each of them missed more after 12 Aug, and from now on a bad week of misses won't drag their rank down.
- **Indirectly:**
  - The overloaded neighbours, The Gale and Sgt. Falkirk, whose load evens out.
  - Nadia's team, which gets an answer for the 45 open tickets.
  - Ravi, who gets an acceptance rate that shows missed and turned down separately.
  - Rook, since we price per active responder.
- **Not fully:** the roughly 11 responders whose pings vanish before they can answer. They stop losing rank, but the pings still vanish until the ping wait is decided.

## Risks
| Risk | What we'd see | How we handle it |
| --- | --- | --- |
| **Too soft on misses.** Wen's 2019 "against" case is that someone who has really stopped taking work keeps getting pinged. | Time-to-accept rises; more callouts go unfilled (they rarely go past the third ping). | A miss still costs something, just less than a turn-down. Wen sets the penalty and recovery rate. Ravi watches time-to-accept and unfilled callouts weekly for the first month. |
| **Wrong cause for some misses.** Misses may be late notifications, not slow answers. | The phone nudge tells responders to check settings that are already fine. | Check delivery times against ping-sent times before launch. If notifications are late, that's its own fix and the nudge copy changes. |
| **Catch-up resets to the wrong number.** Our pre-12 Aug scores come from a replay, not production. | The four come back too high or too low. | Wen pulls the real production scores before the reset. |
| **The neighbours lose work.** The Gale and Sgt. Falkirk picked up the four's pings, and some will go back. This is Priya's "one angry group for another" worry. | Tickets from the other direction. | Say it up front. That work was never theirs by design, and The Gale's handler says The Gale is exhausted. Nadia briefs support before launch. |
| **The card line feels like surveillance.** "9 of 14 missed" could read as a handler scorecard. | Responders feel watched, or handlers push them. | The line explains and never ranks. No scores, no leaderboard. Sofia tests the wording with Kip and one responder. |
| **Timing.** Routing changes ship with the release. Going early is an exception; waiting leaves the four shut out. | Farlight stays at zero pings. | Helen decides: exception or next train. If we wait, the one-time catch-up can go first. |
| **Acceptance rate looks like it jumps.** Splitting missed from turned down changes the weekly report. | Someone reads it as a real change. | Ravi marks the change in the report and shows both series side by side for a few weeks. |
| **Thin evidence.** Data ends 6 Sep, covers 16 responders, and has no previous year to compare. | The pattern doesn't hold once newer data is in. | Ravi re-runs the ping analysis on data since 6 Sep before we commit. |

## Owner and open questions
Marcus Oyelaran's team builds it. Wen Li sets the miss penalty and the recovery rate. Sofia Marino owns the card line and the phone copy. Nadia Hoffmann answers the 45 open callout tickets. Ravi Menon tracks pings per week for the four, plus acceptance rate split by turned down vs missed.

Still open:
- Are the misses slow answers or late notifications?
- Wen's answer to Marcus's 14 Aug question.
- Routing changes normally ship with the release, so does this ride the next train or go as an exception?

## Next steps
1. 30 minutes with Wen and Marcus to agree the miss penalty and recovery rate.
2. A click-through of Kip's card and Mite's phone for you to try.
3. Then the code change.
