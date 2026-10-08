import json
from collections import Counter

with open("mt_text_anno.json", "r", encoding="utf-8") as f:
    data = json.load(f)

positive_patterns = {
    "eyeliner": [
        "eyeliner",
        "winged liner",
        "cat-eye liner",
        "graphic liner",
        "soft liner",
        "subtle liner",
        "gentle liner",
        "heavy liner",
        "tightlin",
        "kohl",
        "waterline lining",
        "eye pencil"
    ],

    "mascara": [
        "mascara",
        "mascaraed",
        "mascared",
        "masacra"
    ],

    "false_lashes": [
        "false lashes",
        "false eyelashes",
        "fake eyelashes",
        "falsies",
        "eyelash extensions"
    ],

    "eyeshadow": [
        "eyeshadow",
        "eye shadow",
        "smoky eye",
        "smokey eye",
        "smoky eyes",
        "smokey eyes",
        "smoky shadow",
        "shimmer shadow"
    ]
}

negative_patterns = {
    "eyeliner": [
        "no eyeliner",
        "no visible eyeliner",
        "no eyeliner visible",
        "no visible wing or heavy liner"
    ],

    "mascara": [
        "no visible mascara"
    ],

    "false_lashes": [
        "no apparent false lashes"
    ],

    "eyeshadow": [
        "no visible eyeshadow",
        "no eyeshadow",
        "no heavy eyeshadow"
    ]
}

counts = Counter()

for image_name, annotations in data.items():

    descriptors = [
        d.lower().strip()
        for d in annotations.get("eye", [])
    ]

    for category in positive_patterns:

        found = False

        for descriptor in descriptors:

            # first check whether this is a negative statement
            if any(
                neg in descriptor
                for neg in negative_patterns[category]
            ):
                continue

            # then check positive patterns
            if any(
                pos in descriptor
                for pos in positive_patterns[category]
            ):
                found = True
                break

        if found:
            counts[category] += 1

total_images = len(data)

print(f"Total images: {total_images}")
print("\nNormalized category frequencies:\n")

for category, count in counts.most_common():
    percentage = count / total_images * 100
    print(f"{category:15s} {count:4d} images ({percentage:.1f}%)")