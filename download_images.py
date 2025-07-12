import os
from duckduckgo_search import DDGS
import requests

# Define your characters and number of images to fetch
characters = {
    "Hua_Cheng": 100,
    "Gojo_Satoru": 100,
    "Emilia": 100,
    "Monkey_D_Luffy": 100,
    "Rintarou_Okabe": 100
}

# Create dataset folders
os.makedirs("dataset", exist_ok=True)
for name in characters:
    os.makedirs(f"dataset/{name}", exist_ok=True)

# Download images using DDGS
with DDGS() as ddgs:
    for name, count in characters.items():
        print(f"🔍 Downloading {count} images of {name}...")
        results = ddgs.images(f"{name} anime face", max_results=count * 2)
        saved = 0
        for res in results:
            if saved >= count:
                break
            url = res["image"]
            try:
                resp = requests.get(url, timeout=5)
                ext = url.split('.')[-1].split('?')[0].lower()
                if ext not in ["jpg", "jpeg", "png"]:
                    continue
                path = f"dataset/{name}/{name}_{saved+1}.{ext}"
                with open(path, "wb") as f:
                    f.write(resp.content)
                saved += 1
            except Exception:
                continue
        print(f"✅ Saved {saved} images to dataset/{name}/")