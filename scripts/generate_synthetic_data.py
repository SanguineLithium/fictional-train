#!/usr/bin/env python3
from __future__ import annotations
import csv, random, hashlib, datetime as dt

random.seed(42)

def fake_email(name: str) -> str:
    base = name.lower().replace(" ", ".")
    dom = random.choice(["example.com", "sample.dev", "demo.org"])
    return f"{base}@{dom}"

def hash_id(*parts: str) -> str:
    s = "|".join(parts)
    return hashlib.sha256(s.encode()).hexdigest()[:12]

def main(path: str = "data/synthetic_customers.csv", n: int = 1000):
    first = ["Avery","Jordan","Taylor","Riley","Casey","Morgan","Alex","Jamie","Quinn","Rowan"]
    last  = ["Nguyen","Patel","Kim","Garcia","Brown","Lopez","Martin","Lee","Chen","Davis"]
    segments = ["self-serve","smb","enterprise"]
    rows = []
    base = dt.date(2023,1,1)

    for i in range(n):
        name = f"{random.choice(first)} {random.choice(last)}"
        seg = random.choices(segments, weights=[0.5,0.35,0.15])[0]
        signup = base + dt.timedelta(days=random.randint(0, 640))
        usage_hours = max(0, random.gauss(mu={"self-serve":3,"smb":8,"enterprise":20}[seg], sigma=2))
        ai_assist_calls = int(max(0, random.gauss(mu={"self-serve":5,"smb":25,"enterprise":80}[seg], sigma=10)))
        churned = int(random.random() < {"self-serve":0.18,"smb":0.10,"enterprise":0.06}[seg])

        rows.append({
            "customer_id": hash_id(name, str(signup)),
            "name": name,
            "email": fake_email(name),
            "segment": seg,
            "signup_date": signup.isoformat(),
            "monthly_usage_hours": round(usage_hours, 1),
            "monthly_ai_assist_calls": ai_assist_calls,
            "churned": churned
        })

    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {path}")

if __name__ == "__main__":
    main()
