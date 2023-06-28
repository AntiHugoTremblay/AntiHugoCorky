import weechat as w
from collections import deque as dq

w.register("hugay", "LUEshi", "1.0", "MIT", "Hugo Tremblay est une megatrouducul", "", "")

MHS = 10
ST = 3
MET = 300
mh, mc = dq(maxlen=MHS), {}

def as_cb(d, b, dt, t, dp, h, p, m):
    global mh, mc
    ct = int(dt)
    while mh and ct - mh[0]['time'] > MET: o_m = mh.popleft(); mc[o_m['content']] -= 1; mc.pop(o_m['content'], None)
    mc[m] = mc[m] + 1 if m in mc else 1
    if mc[m] >= ST: w.prnt("", f"Spam message removed: {m}"); return w.WEECHAT_RC_OK_EAT
    mh.append({'time': ct, 'content': m})
    return w.WEECHAT_RC_OK

w.hook_print("", "irc_privmsg", "", 1, "as_cb", "")
