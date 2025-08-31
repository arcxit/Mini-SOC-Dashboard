import re
from pathlib import Path
import pandas as pd

FAIL_PAT = re.compile(r"Failed password.*from\s+(\d+\.\d+\.\d+\.\d+)")

def parse_authlog(path="sample_logs/auth.log"):
    p = Path(path)
    if not p.exists():
        return pd.DataFrame(columns=["ip", "count"])
    ips = []
    with p.open(errors="ignore") as f:
        for line in f:
            m = FAIL_PAT.search(line)
            if m:
                ips.append(m.group(1))
    if not ips:
        return pd.DataFrame(columns=["ip", "count"])
    df = pd.Series(ips).value_counts().reset_index()
    df.columns = ["ip", "count"]
    return df

def summary(df: pd.DataFrame):
    total_fails = int(df["count"].sum()) if not df.empty else 0
    top = df.head(10).to_dict(orient="records") if not df.empty else []
    return {"total_failed_logins": total_fails, "top_sources": top}
