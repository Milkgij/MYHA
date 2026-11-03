# MYHA — Tinkers' Construct → Horizon

Experimental **partial** content port for [Horizon](https://github.com/horizon-rust/horizon) API 0.2, using the user's TConstruct 1.20.1-3.11.2.166 Forge JAR.

## Build (Windows / PowerShell)

Install Python 3.10+. Download your own original TConstruct JAR, place it beside the script, then run:

```powershell
py -3 port_tconstruct.py ".\TConstruct-1.20.1-3.11.2.166.jar"
```

Output: `build/tconstruct_horizon_partial.hmod`. Install it in Horizon's game folder under `horizon-mods/`, enable it in Options → Mods and restart. Validate with the official CLI:

```powershell
cargo install --git https://github.com/horizon-rust/horizon cargo-horizon-mod
cargo horizon-mod check build/tconstruct_horizon_partial.hmod
```

**Status:** only simple materials, shards, nuggets and casting item graphics are converted to content registry entries. Items inherit vanilla paper behaviour as placeholders. No smeltery, casting logic, tool assembly, custom combat, modifiers, multiblock structures, fluids, block entities, recipes, or worldgen. The Minecraft 1.20.1 assets may need further adaptation for 26.3. **No in-game compatibility test has been performed.** Back up worlds before testing.

Complex features require a separate native `.hnmod` Rust implementation using [horizon-mixins](https://github.com/horizon-rust/horizon-mixins). This is not a JAR loader or an equivalent replacement for the Forge mod.

Original TConstruct metadata declares MIT license; original credit: SlimeKnights. This repository does **not** commit copied proprietary jars or extracted resources; generate locally from your own copy and check applicable third-party credits before redistribution.
