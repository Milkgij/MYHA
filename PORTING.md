# NeoForge 1.21.1 port verification

Target: Minecraft **1.21.1**, **NeoForge 21.1.x**, **Java 21**.

Supplied reference JAR: `TConstruct-1.20.1-3.11.2.166.jar` (Minecraft 1.20.1 Forge, Mantle >= 1.11.97). The imported source is a distinct community revision; it is not guaranteed to contain all changes from binary version 3.11.2.166.

- [ ] Import complete Java source, resources, data packs, and Gradle wrapper to `neoforge-1.21.1`.
- [ ] Compile `assemble` and verify that the JAR includes `META-INF/neoforge.mods.toml`.
- [ ] Run unit tests (`./gradlew test`).
- [ ] Launch in NeoForge 1.21.1 and verify registries, GUIs, creative tabs, item tooltips.
- [ ] Test material and part crafting, modular tools, tools modifiers, and repair.
- [ ] Test smeltery and foundry multiblocks, fluids, alloying, and casting.
- [ ] Test dedicated server and client, save/reload, recipes, data pack compatibility.
- [ ] Compare behavior and content with source reference JAR 3.11.2.166.

A successful build **only establishes compilation**, not complete gameplay correctness.
