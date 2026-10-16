"""Replay the four shut-out responders' acceptance scores under 4.2's rules
and under the proposed fix, then estimate their weekly home-area pings
with the fix in place. Data copied from rook-database (pings, callouts).
"""
import json, random
from datetime import datetime, timedelta

SEQ = {
 "Farlight": "06300737Th,06302354Do,07010852Th,07011127Do,07011130Dh,07012052Th,07012117Th,07012154Th,07020834Th,07020903Th,07031609Th,07040050Th,07060425Th,07070959Th,07080009Dh,07081349Th,07090816Th,07091847Th,07091941Do,07092011Do,07092121Th,07110846Th,07111402Th,07121537Th,07131531Th,07132321Mo,07150505Th,07152326Th,07161420Th,07161906Th,07170815Do,07181834Do,07181934Th,07182117Th,07182318Th,07201034Th,07201131Th,07210744Th,07211050Th,07221727Mo,07221848Th,07232152Th,07232330Do,07240451Th,07241331Dh,07241937Th,07250004Th,07271233Th,07271319Th,07282254Do,07291727Th,07302150Th,07310800Th,08010108Th,08011548Th,08012330Dh,08020918Th,08021100Do,08021844Th,08022054Th,08031544Do,08042001Th,08050529Th,08050945Th,08051626Th,08051945Th,08061220Th,08071235Do,08071842Th,08080021Mo,08081039Th,08082019Do,08101538Th,08101734Th,08102108Do,08121636Th,08121951Mo,08122002Do,08130945Mh,08131451Mo,08141632Mh,08142122Th,08191328Mh,08221113Dh,08231351Mo,08281928Mo",
 "Meteor Mite": "07010842Th,07011500Dh,07020113Th,07020544Th,07031822Th,07040857Dh,07041156Do,07041447Dh,07042334Th,07051218Th,07051817Th,07061515Th,07071144Th,07071717Th,07072259Th,07080848Th,07081944Th,07101818Do,07101841Th,07112030Dh,07121321Th,07121851Th,07122359Do,07130914Th,07131047Dh,07131920Th,07140733Dh,07151234Th,07172101Th,07190846Th,07190910Th,07192059Do,07192248Do,07201625Th,07201821Th,07230948Mh,07231042Dh,07231932Th,07232119Th,07241233Th,07241716Dh,07241913Dh,07250908Th,07251036Th,07270047Th,07271610Th,07271813Th,07281906Th,07281946Mh,07282230Th,07301710Th,07301851Do,07302125Th,08011014Th,08021546Th,08021912Dh,08031934Th,08042034Th,08051347Dh,08051453Th,08060114Do,08060121Th,08060502Do,08061620Th,08080754Th,08081655Th,08082043Th,08101403Dh,08102115Th,08110641Th,08121904Do,08131343Mo,08131512Mh,08140726Mh,08151518Th,08151940Th,08161116Mh,08180737Dh,08191730Th,08201641Mh,08222053Mo,08272003Do,08290915Mh,09051506Mo",
 "The Undertow": "06290543Th,06290726Th,06291352Do,06291431Th,06291517Th,06291818Do,06300858Do,07011044Th,07011924Th,07031730Th,07031745Th,07041229Th,07061636Th,07071417Dh,07071709Th,07071719Th,07082007Th,07082125Th,07090235Th,07090837Dh,07092132Th,07100739Th,07111610Th,07130401Th,07132021Mo,07151304Th,07151553Th,07161744Th,07161956Th,07162135Th,07171752Do,07171755Do,07171802Th,07171847Th,07180743Th,07200136Dh,07200657Dh,07201620Th,07201802Th,07201809Th,07221823Th,07222235Th,07231528Th,07231902Th,07251216Th,07260032Th,07260617Do,07261945Th,07270854Th,07271116Th,07280932Th,07281752Th,07290404Th,07290631Th,07291657Th,07311822Th,07312007Do,08010807Do,08011405Th,08011847Th,08041025Th,08041243Dh,08051745Th,08051818Th,08052054Do,08060049Th,08070426Do,08071029Th,08071951Th,08072212Th,08072313Th,08081358Th,08101849Th,08101945Th,08111858Do,08120904Mo,08131124Mh,08131328Th,08131555Th,08131844Mh,08140253Mo,08141022Mo,08161346Do,08171410Do,08171907Th,08181618Mh,08211645Mh,08272318Mh,09051517Mh",
 "Vesper": "06290005Th,06301505Do,06301917Th,07011329Th,07011925Th,07012017Th,07020843Th,07021538Th,07030728Th,07031451Th,07032011Do,07040100Th,07041416Th,07052204Dh,07060846Th,07070200Mo,07071839Th,07072056Th,07081710Th,07092300Th,07111347Th,07111416Do,07111503Th,07112120Th,07112129Do,07121055Th,07121607Th,07130210Th,07131824Th,07131839Th,07141911Th,07151208Th,07151950Th,07151957Th,07161902Do,07162125Th,07171726Th,07171927Mo,07172015Th,07191350Th,07191558Th,07191937Th,07200946Do,07201013Do,07202119Th,07220155Th,07221120Th,07221128Th,07221656Th,07221822Th,07231656Th,07240109Th,07251550Th,07251914Do,07260105Th,07262308Th,07270833Th,07272046Th,07280721Th,07281133Th,07281448Th,07290331Th,07300229Mo,07300748Th,07301324Th,07302317Th,07311128Th,07311659Th,08011912Do,08040644Th,08041509Th,08041516Th,08041804Th,08051650Th,08052025Th,08060548Th,08060943Th,08061215Do,08061748Th,08071257Th,08071707Th,08071755Do,08081951Th,08100201Th,08101333Dh,08112100Th,08130734Mo,08140253Th,08141710Mo,08151302Th,08151533Do,08152058Th,08161046Mo,08161405Mo,08161603Th,08170855Th,08191842Mh,08230010Mh,08230534Do,08232015Mo,08242140Dh,08261809Mh,09011142Mh",
}
# Home-area callouts from 12 Aug on.
CALLOUTS = {
 "Farlight": "08-12 16:35,08-13 09:45,08-14 16:32,08-14 21:22,08-17 12:04,08-17 19:00,08-18 18:47,08-19 13:27,08-19 21:38,08-20 22:41,08-22 11:13,08-24 03:27,08-24 14:36,08-25 19:35,08-25 23:50,08-27 10:37,08-29 19:13,08-30 10:18,08-30 13:59,08-30 15:08,08-30 19:46,08-31 15:03,08-31 16:44,08-31 17:42,08-31 19:50,09-03 12:42,09-03 13:53,09-03 22:37,09-04 12:18,09-04 19:26,09-06 15:21",
 "Meteor Mite": "08-13 15:12,08-14 07:26,08-14 11:44,08-14 22:43,08-15 15:17,08-15 19:38,08-16 09:43,08-16 11:16,08-16 23:19,08-17 17:03,08-17 19:21,08-17 20:56,08-17 22:35,08-18 07:36,08-18 10:46,08-19 17:29,08-20 12:35,08-20 16:41,08-21 17:09,08-21 21:58,08-22 11:45,08-22 12:25,08-23 10:07,08-23 18:34,08-24 17:11,08-24 18:59,08-25 01:53,08-25 11:18,08-25 12:09,08-26 09:40,08-26 12:33,08-28 05:10,08-28 17:03,08-28 17:28,08-28 21:15,08-29 09:15,08-30 05:05,08-30 18:26,08-30 19:28,08-30 19:40,08-31 10:36,09-01 07:55,09-01 17:56,09-01 18:57,09-02 15:29,09-03 12:40,09-03 16:57,09-04 06:27,09-04 07:13,09-04 08:52,09-04 16:33,09-04 21:47,09-05 12:15,09-05 13:13,09-05 16:00,09-05 17:56,09-05 19:57",
 "The Undertow": "08-13 11:24,08-13 13:26,08-13 15:54,08-13 18:44,08-17 19:06,08-18 15:29,08-18 16:17,08-20 05:17,08-21 16:45,08-23 20:17,08-23 21:02,08-24 10:45,08-24 13:20,08-25 01:20,08-26 21:22,08-27 23:18,08-28 03:20,08-28 21:49,08-28 21:50,08-30 16:31,08-30 20:06,08-31 16:53,09-01 11:08,09-02 13:47,09-02 16:27,09-03 20:10,09-03 20:48,09-04 17:04,09-05 10:51,09-05 15:17,09-05 15:19,09-05 18:49",
 "Vesper": "08-14 02:52,08-15 13:01,08-15 20:55,08-16 16:03,08-17 08:54,08-18 15:29,08-19 18:42,08-21 22:54,08-22 02:24,08-22 11:42,08-22 17:51,08-23 00:10,08-24 16:51,08-24 17:03,08-24 20:13,08-24 21:40,08-26 18:08,08-26 19:05,08-27 19:10,08-27 19:42,08-28 18:57,08-28 20:24,08-30 11:26,08-30 20:39,08-31 21:50,09-01 11:15,09-01 11:42,09-02 14:45,09-03 11:10,09-03 13:08,09-04 09:34,09-04 11:54,09-05 07:22,09-05 13:03,09-05 18:30,09-06 07:55,09-06 08:08,09-06 09:42",
}
# Home-area callouts and home pings per week before 4.2 (weeks of 29 Jun – 3 Aug).
PRE_HOME = {"Farlight": (57, 57), "Meteor Mite": (112, 59), "The Undertow": (61, 61), "Vesper": (69, 69)}

RELEASE = datetime(2026, 8, 12)
WEEKS = [datetime(2026, 8, 10) + timedelta(days=7 * k) for k in range(4)]  # 10, 17, 24, 31 Aug

CREDIT, DECLINE = 0.08, 0.12
FIX_MISS = 0.03          # proposed: a miss costs a quarter of a turn-down
FIX_RECOVERY = 0.05      # proposed: each day, close 5% of the gap to neutral (0.5)
NEUTRAL, FLOOR, CEIL = 0.5, 0.0, 1.0
TYPICAL = {"T": 0.64, "D": 0.18, "M": 0.18}  # all responders after 12 Aug


def parse(seq):
    out = []
    for item in seq.split(","):
        t = datetime(2026, int(item[0:2]), int(item[2:4]), int(item[4:6]), int(item[6:8]))
        out.append((t, item[8], item[9]))
    return out


def clamp(x):
    return max(FLOOR, min(CEIL, x))


def step(score, outcome, fix):
    if outcome == "T":
        return clamp(score + CREDIT)
    if outcome == "D" or not fix:
        return clamp(score - DECLINE)
    return clamp(score - FIX_MISS)


def recover(score, days):
    # Only lifts a low score back toward neutral; never pulls a good score down.
    if score >= NEUTRAL:
        return score
    return NEUTRAL + (score - NEUTRAL) * (1 - FIX_RECOVERY) ** days


def score_before(pings, until):
    """Replay real pings up to `until` under the pre-fix rules."""
    s = NEUTRAL
    for t, o, _ in pings:
        if t >= until:
            break
        s = step(s, o, fix=False)
    return s


def calibrate(all_pings, callouts_by_name):
    """How often a responder is pinged for a home-area callout, by score band,
    measured on the real data under 4.2's rules (score replayed from real pings)."""
    bands = {"high": [0, 0], "mid": [0, 0], "low": [0, 0]}
    def band(s):
        return "high" if s >= 0.6 else "mid" if s >= 0.4 else "low"
    for name, pings in all_pings.items():
        home_ping_times = [t for t, _, h in pings if h == "h" and t >= RELEASE]
        for c in callouts_by_name[name]:
            s = score_before(pings, c)
            b = band(s)
            bands[b][0] += 1
            if any(abs((t - c).total_seconds()) <= 300 for t in home_ping_times):
                bands[b][1] += 1
    return {k: (v[1] / v[0] if v[0] else None, v[0]) for k, v in bands.items()}, band


def week_index(t):
    for k in range(len(WEEKS) - 1, -1, -1):
        if t >= WEEKS[k]:
            return k
    return None


def simulate(name, pings, callouts, rates, p_ping, band, fix, runs=4000, seed=7):
    rng = random.Random(seed)
    start = score_before(pings, RELEASE)
    # Home pings in the release week before 12 Aug are real, not simulated.
    real_pre = sum(1 for t, _, h in pings if h == "h" and WEEKS[0] <= t < RELEASE)
    totals = [0.0] * len(WEEKS)
    for _ in range(runs):
        s, last = start, RELEASE
        counts = [0] * len(WEEKS)
        counts[0] += real_pre
        for c in callouts:
            if fix:
                s = recover(s, (c - last).total_seconds() / 86400)
            last = c
            if rng.random() < p_ping[band(s)]:
                counts[week_index(c)] += 1
                r = rng.random()
                o = "T" if r < rates["T"] else "D" if r < rates["T"] + rates["D"] else "M"
                s = step(s, o, fix)
        for k in range(len(WEEKS)):
            totals[k] += counts[k]
    return [round(x / runs, 1) for x in totals]


def main():
    all_pings = {n: parse(s) for n, s in SEQ.items()}
    callouts = {n: [datetime.strptime("2026-" + c, "%Y-%m-%d %H:%M") for c in s.split(",")] for n, s in CALLOUTS.items()}
    cal, band = calibrate(all_pings, callouts)
    # High band also includes the pre-release weeks, where everyone sat near the ceiling.
    pre_c = sum(v[0] for v in PRE_HOME.values()); pre_p = sum(v[1] for v in PRE_HOME.values())
    print("calibration (post-12 Aug, 4.2 scores):", cal, " pre-release home ping rate:", round(pre_p / pre_c, 2))

    result = {}
    for name, pings in all_pings.items():
        pre_rate = PRE_HOME[name][1] / PRE_HOME[name][0]
        # Scale the measured band rates to each responder's own pre-release share
        # (Meteor Mite shares Eastgate with The Gale, so her share is about half).
        overall_high = cal["high"][0] or pre_p / pre_c
        p_ping = {b: min(1.0, (cal[b][0] if cal[b][0] is not None else 0) / overall_high * pre_rate) for b in cal}
        p_ping["high"] = pre_rate
        post = [o for t, o, _ in pings if t >= RELEASE]
        own = {k: post.count(k) / len(post) for k in "TDM"}
        actual = [sum(1 for t, _, h in pings if h == "h" and week_index(t) == k and t >= WEEKS[0]) for k in range(len(WEEKS))]
        result[name] = {
            "start_score": round(score_before(pings, RELEASE), 2),
            "p_ping": {k: round(v, 2) for k, v in p_ping.items()},
            "own_rates": {k: round(v, 2) for k, v in own.items()},
            "actual_home": actual,
            "model_42_own": simulate(name, pings, callouts[name], own, p_ping, band, fix=False),
            "fix_own": simulate(name, pings, callouts[name], own, p_ping, band, fix=True),
            "fix_typical": simulate(name, pings, callouts[name], TYPICAL, p_ping, band, fix=True),
            "home_callouts": [sum(1 for c in callouts[name] if week_index(c) == k) for k in range(len(WEEKS))],
        }
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
