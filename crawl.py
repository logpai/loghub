import json
import os
import regex as re

f = open("zenodo_page.txt", encoding="utf-8")
data = f.read().replace("\n", " ")
print("zenodo_page.txt:", data)
downloads = re.findall(r'"stats": {"all_versions": .*?"unique_downloads": ([\d,]+), ', data)[0]
downloads = '{:,}'.format(int(downloads))
print("Crawled downloads:", downloads)

shieldio_dict = {
  "schemaVersion": 1,
  "label": "Downloads",
  "message": downloads,
}
with open(f'downloads.json', 'w') as outfile:
    json.dump(shieldio_dict, outfile, ensure_ascii=False)
