import os
from pathlib import Path

entry = "I invited the leftovers back for dinner. They have great reheat-ability."
out = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(entry, encoding="utf-8")
