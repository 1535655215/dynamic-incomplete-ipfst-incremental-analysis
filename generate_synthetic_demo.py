from pathlib import Path
import csv
from model import generate_table, full_ap1

OUT = Path(__file__).parent / "data"
OUT.mkdir(exist_ok=True)
rows = []
for n, m in [(100, 10), (300, 30), (1000, 10)]:
    for seed in [20261020, 20261021, 20261022]:
        _, _, _, w, c = full_ap1(generate_table(n, m, seed))
        rows.append({"n": n, "m": m, "seed": seed,
                     "weight_sum": f"{w.sum():.17g}",
                     "conflict_mean": f"{c.mean():.17g}"})
with (OUT / "synthetic_reference_outputs.csv").open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0])
    writer.writeheader()
    writer.writerows(rows)
print(OUT / "synthetic_reference_outputs.csv")
