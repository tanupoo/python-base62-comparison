import re

# only ff
cn = None
ed = {}
dd = {}
with open("README.md") as fd:
    for line in fd:
        if re.match("^\#\# Measurement", line):
            break
    for line in fd:
        r = re.match("^## Timeit: (\w+) encoding", line)
        if r:
            cn = r.group(1)
            ep = ed.setdefault(cn, {})
            continue
        # data/ff128.dmp 1.192028757
        r = re.match("^data/ff(\d+).dmp\s([\d\.]+)", line)
        if r:
            ep.update({r.group(1):r.group(2)})
            continue
        r = re.match("^## Timeit: (\w+) decoding", line)
        if r:
            cn = r.group(1)
            dp = dd.setdefault(cn, {})
            continue
        # data/ff128en-BG.txt 2.940678835
        r = re.match("^data/ff(\d+)en-(\w+).txt\s([\d\.]+)", line)
        if r:
            if cn != r.group(2):
                raise ValueError(f"{cn} != {r.group(2)}")
            dp.update({r.group(1):r.group(3)})
            continue

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(8, 6))

ax = fig.add_subplot(1,2,1)
for cn,vals in ed.items():
    xp = []
    yp = []
    for x,y in vals.items():
        xp.append(int(x))
        yp.append(float(y))
    ax.plot(xp, yp, label=f"{cn}")
ax.set_xticks([128,256,512,768,1024,1536,2048])
ax.set_xlabel("Original data size (B)", fontsize=12)
ax.set_ylabel("Process time (sec)", fontsize=12)
ax.set_title("Encoding speed")
ax.grid()
ax.legend()

ax = fig.add_subplot(1,2,2)
for cn,vals in dd.items():
    xp = []
    yp = []
    for x,y in vals.items():
        xp.append(int(x))
        yp.append(float(y))
    ax.plot(xp, yp, label=f"{cn}")
ax.set_xticks([128,256,512,768,1024,1536,2048])
ax.set_xlabel("Original data size (B)", fontsize=12)
ax.set_ylabel("Process time (sec)", fontsize=12)
ax.set_title("Decoding speed")
ax.grid()
ax.legend()

plt.subplots_adjust(wspace=0.4)
plt.savefig("timeit.png")
plt.show()
