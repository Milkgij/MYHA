# MYHA — Tinkers' Construct for NeoForge 1.21.1

This repository is a workspace for testing an **unofficial source port** of Tinkers' Construct for **Minecraft 1.21.1, NeoForge 21.1.x, Java 21**.

The supplied original `TConstruct-1.20.1-3.11.2.166.jar` is a compiled Minecraft 1.20.1 **Forge** mod. Renaming or editing its `mods.toml` does not port its Java code.

## Source code and builds

The workflow [Import Tinkers source and build](.github/workflows/import-tconstruct.yml) imports an existing MIT-licensed community source port into a separate **`neoforge-1.21.1` branch**, preserving the default `main` branch.

Pinned source:
- https://github.com/Zazow/TinkersConstruct-1.21.1, branch `1.21.1`
- Commit `1c98a9e43115931574b8017193b2c48982aa184d`

This is **an existing third-party port**, not a fully new port of the uploaded 3.11.2.166 binary. Compilation, gameplay parity, stability, and compatibility with existing worlds are **not guaranteed**.

To get a build if compilation succeeds: open [Actions](../../actions) → **Import Tinkers source and build** → latest successful run → **Artifacts**. Download and extract the generated mod JAR. Later changes to the imported branch use [NeoForge 1.21.1 build](.github/workflows/neoforge-build.yml).

If there is no artifact or the run fails, the build is **not verified**. Do not use the original Forge JAR on NeoForge 1.21.1.

## Important compatibility note

[Horizon](https://github.com/horizon-rust/horizon) is a standalone Minecraft rewrite in Rust, **not NeoForge**. It does **not** load Java mod JARs. A native Horizon version requires a separate implementation.

## Credits

Original Tinkers' Construct © SlimeKnights and contributors (MIT).
Community NeoForge port by Zazow and contributors (MIT).
Existing MYHA repository metadata © Milkgij (MIT). The source-import workflow preserves the original upstream MIT LICENSE and a copy of MYHA's initial license. This is an unofficial project, not endorsed by the original authors.

See [PORTING.md](PORTING.md) for the testing checklist.
