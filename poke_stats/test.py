import numpy as np
import pandas as pd
import requests
import datetime as dt
from showdown_stats import PokemonStats
import seaborn as sns
import matplotlib.pyplot as plt
from MDate import MDate

poke = PokemonStats("Rillaboom")
poke.get_stats("vgc", 2019, 10)
data = poke.full_data[poke.full_data["rating"] == 0]
sns.set(rc={'figure.figsize':(14, 12)})
sns.barplot(x=data.index, y="usage_amount", data=data, ci=None)
plt.title("{} Usage".format(poke.name))
plt.xlabel("Month")
plt.xticks(rotation=90)
plt.ylabel("Usage amount")
plt.tight_layout()
plt.show()