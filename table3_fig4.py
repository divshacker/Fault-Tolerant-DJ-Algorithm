"""Recompute Table III and Fig. 4 of arXiv:2412.04791 from the raw counts in
https://github.com/divshacker/Fault-Tolerant-DJ-Algorithm  (Experimental-Results/).
Usage: python table3_fig4.py /path/to/Fault-Tolerant-DJ-Algorithm"""
import json, math, sys, os
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.stats import fisher_exact

repo = sys.argv[1] if len(sys.argv) > 1 else "."
N = 4096
P1 = {1: 1, 2: 0, 3: 0, 4: 1}            # ideal P_1: 1 for constant, 0 for balanced
labels = ["$f(x)=0$", "$f(x)=x$", r"$f(x)=1\oplus x$", "$f(x)=1$"]
ONE = {"1010", "0101", "0110", "1001"}    # logical R_1 outcomes, eq. (4)

rows, Sb, Se, Vb, Ve = [], 0, 0, 0, 0
for i in range(1, 5):
    bare = json.load(open(os.path.join(repo, "Experimental-Results/Bare Circuit Results", f"bare_deutsch_d{i}.json")))
    hist = {tuple(h["Outcome"]): h["Count"] for h in bare["Results"][0]["Histogram"]}
    wrong_b = sum(v for k, v in hist.items() if k[1] != P1[i])      # output qubit = 2nd entry
    enc = json.load(open(os.path.join(repo, "Experimental-Results/Encoded Circuit Results", f"encoded_deutsch_d{i}.json")))
    cnt = {k: round(p * N) for k, p in enc["measurementProbabilities"].items()}
    kept = {k: v for k, v in cnt.items() if k.count("1") % 2 == 0}  # post-selection
    Ne = sum(kept.values())
    wrong_e = sum(v for k, v in kept.items() if (k in ONE) != bool(P1[i]))
    Db, De = wrong_b / N, wrong_e / Ne                               # D = P(wrong answer)
    sb, se = math.sqrt(Db * (1 - Db) / N), math.sqrt(De * (1 - De) / Ne)
    sd = math.hypot(sb, se)
    red = (De - Db) / Db
    sred = math.sqrt((se / Db) ** 2 + (De * sb / Db ** 2) ** 2)
    p = fisher_exact([[wrong_b, N - wrong_b], [wrong_e, Ne - wrong_e]], alternative="greater")[1]
    rows.append((labels[i - 1], Db, sb, De, se, De - Db, sd, Ne / N, 100 * red, 100 * sred, (Db - De) / sd, p, wrong_b, wrong_e, Ne))
    Sb += Db; Se += De; Vb += sb ** 2; Ve += se ** 2

for r in rows:
    print("{:18s} Db={:.5f}±{:.5f} De={:.5f}±{:.5f} diff={:+.5f}±{:.5f} PS={:.3f} "
          "red={:.1f}±{:.1f}% z={:.1f} Fisher p={:.2g} wrong {}/4096 vs {}/{}".format(*r))
pooled = Se / Sb - 1
spooled = math.sqrt(Ve / Sb ** 2 + (Se / Sb ** 2) ** 2 * Vb)
print(f"pooled (sum D_enc / sum D_bare - 1) = {100*pooled:.1f} ± {100*spooled:.1f} %,  z = {(Sb-Se)/math.sqrt(Vb+Ve):.1f}")
print(f"unweighted mean of per-oracle reductions = {sum(r[8] for r in rows)/4:.1f} %")

fig, ax = plt.subplots(figsize=(5.5, 4))
x = range(4)
ax.bar(x, [r[8] for r in rows], color="grey")
ax.errorbar(x, [r[8] for r in rows], yerr=[r[9] for r in rows], fmt="o", color="black", capsize=0, lw=1.5)
ax.set_xticks(list(x)); ax.set_xticklabels([r[0] for r in rows])
ax.set_ylim(-120, 0); ax.set_xlabel("Oracle"); ax.set_ylabel("Noise Reduction (%)")
fig.tight_layout(); fig.savefig("percentage-noise-reduction.pdf")
