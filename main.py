from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd

from models.performance_model import compute_ctl_atl
from models.session import TrainingSession
from models.sport_weight import weighted_load
from models.training_load import compute_trimp

# Exemple données
sessions = [
    TrainingSession(datetime(2026, 2, 1), "run", 60, 150, 190, 50),
    TrainingSession(datetime(2026, 2, 2), "bike", 90, 140, 190, 50),
    TrainingSession(datetime(2026, 2, 3), "trail", 120, 155, 190, 50),
]

data = []

for s in sessions:
    trimp = compute_trimp(s.duration_min, s.avg_hr, s.hr_rest, s.hr_max)
    load = weighted_load(trimp, s.sport)

    data.append([s.date, load])

df = pd.DataFrame(data, columns=["date", "load"])
df = df.set_index("date")

ctl, atl, tsb = compute_ctl_atl(df["load"])

print(ctl)
print(tsb)

ctl.plot(label="CTL")
atl.plot(label="ATL")
tsb.plot(label="TSB")

plt.legend()
plt.show()
