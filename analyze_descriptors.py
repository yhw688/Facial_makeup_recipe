import json
from collections import Counter

with open("mt_text_anno.json", "r", encoding="utf-8") as f:
    data = json.load(f)

eye_descriptors = Counter()

for image_name, annotations in data.items():
    for descriptor in annotations.get("eye", []):
        eye_descriptors[descriptor.lower().strip()] += 1

print(f"Total images: {len(data)}")
print(f"Unique eye descriptors: {len(eye_descriptors)}")

with open("all_eye_descriptors.txt", "w", encoding="utf-8") as f:
    for descriptor, count in eye_descriptors.most_common():
        f.write(f"{descriptor}\t{count}\n")

print("Saved all descriptors to all_eye_descriptors.txt")