#!/usr/bin/env python3
"""Experimental TConstruct Forge 1.20.1 to Horizon API 0.2 item-only port."""
import argparse, json, re, shutil, zipfile
from pathlib import Path

PREFIX = "assets/tconstruct/models/item/"
SUFFIXES = ("_ingot", "_nugget", "_shard", "_cluster", "_reinforcement", "_cast", "_sand_cast", "_red_sand_cast", "_slime_ball", "_slime_crystal")
EXTRAS = {"dragon_scale", "copper_gauge", "modifier_crystal", "blood_slime_ball", "ender_slime_ball", "bacon"}

def write_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def convert(jar, dest, limit=0):
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    converted, skipped = [], []
    with zipfile.ZipFile(jar) as src:
        names = set(src.namelist())
        english = json.loads(src.read("assets/tconstruct/lang/en_us.json"))
        russian = json.loads(src.read("assets/tconstruct/lang/ru_ru.json")) if "assets/tconstruct/lang/ru_ru.json" in names else {}
        for path in sorted(p for p in names if p.startswith(PREFIX) and p.endswith(".json")):
            item = path[len(PREFIX):-5]
            if "/" in item or not re.fullmatch("[a-z0-9_]+", item):
                continue
            if not (item.endswith(SUFFIXES) or item in EXTRAS):
                continue
            if limit and len(converted) >= limit:
                break
            model = json.loads(src.read(path))
            tex = model.get("textures", {}).get("layer0")
            if model.get("parent") not in ("item/generated", "minecraft:item/generated") or not isinstance(tex, str) or not tex.startswith("tconstruct:item/"):
                skipped.append([item, "unsupported model"])
                continue
            png = "assets/tconstruct/textures/item/" + tex.split("tconstruct:item/", 1)[1] + ".png"
            if png not in names:
                skipped.append([item, "missing texture"])
                continue
            write_json(dest / "data/tconstruct/horizon/item" / (item + ".json"), {"template": "minecraft:paper"})
            write_json(dest / "assets/tconstruct/items" / (item + ".json"), {"model": {"type": "minecraft:model", "model": "tconstruct:item/" + item}})
            write_json(dest / path, model)
            asset = dest / png
            asset.parent.mkdir(parents=True, exist_ok=True)
            asset.write_bytes(src.read(png))
            converted.append(item)
        if not converted:
            raise ValueError("No supported material items found")
        for loc, lang in (("en_us", english), ("ru_ru", russian)):
            write_json(dest / "assets/tconstruct/lang" / (loc + ".json"),
                       {"item.tconstruct." + item: lang.get("item.tconstruct." + item, item.replace("_", " ").title()) for item in converted})
        (dest / "horizon-mod.toml").write_text('''id = "tconstruct"
name = "Tinkers Construct Horizon content prototype"
version = "0.1.0"
description = "Partial item-only port; no smeltery or tool modifiers."
authors = ["SlimeKnights (original)", "MYHA (port)"]
api = "0.2"
side = "both"
capabilities = ["registries"]
''', encoding="utf-8")
        write_json(dest / "PORT_REPORT.json", {"items": len(converted), "ids": converted, "skipped": skipped, "gameplay_implemented": False})
    return converted

def pack(folder, output):
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as out:
        for file in sorted(folder.rglob("*")):
            if file.is_file():
                rel = file.relative_to(folder).as_posix()
                if rel == "horizon-mod.toml" or rel.startswith(("assets/", "data/")):
                    out.write(file, rel)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("jar", type=Path)
    parser.add_argument("--out", type=Path, default=Path("build/tconstruct"))
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    items = convert(args.jar, args.out, args.limit)
    artifact = args.out.parent / "tconstruct_horizon_partial.hmod"
    pack(args.out, artifact)
    print(f"Generated {artifact}: {len(items)} basic item registrations. NOT a complete gameplay port.")
