# HOC — LANDMARK_MINE_NEUTRAL_01

Status: **CANDIDATE A FROZEN — BINARY MATERIALIZATION ONLY**

This candidate is the production gate for Tehkné Assets Forge issue #7 and Hexa Octarina Conquer #413.

The generated presentation sheet is not an asset and is excluded from production. The isolated Mine render is Candidate A and is now frozen: no further Mine generation is allowed unless the HOC gameplay-scale review explicitly rejects this exact asset.

## Canonical Candidate A

- canonical ID: `LANDMARK_MINE_NEUTRAL_01`;
- family: `WORLD_LANDMARKS / EXTRACTION / MINE`;
- canonical path: `art/LANDMARK_MINE_NEUTRAL_01.png`;
- normalized canvas: `2048 × 2048` RGBA;
- fully transparent canvas coverage: `57.2248%`;
- nontransparent bbox (`alpha > 20`): `64,544 → 1984,1984`;
- bottom margin: `64 px`;
- horizontal safety margins: `64 px`;
- pivot contract: bottom-center;
- exact PNG SHA-256: `9014411a8c81b89adc3c4ba52b5a3fafd4ad925c7033699c5590e94d36749069`;
- exact PNG size: `4,524,328 bytes`;
- neutral stone/timber/iron/earth palette with no Blue/Red ownership coding;
- no baked text, UI, marker, badge, frame, logo or HUD treatment.

## Semantic result

Candidate A reads as a **constructed extraction installation** through a combined authored silhouette:

1. reinforced mine portal embedded in rock;
2. timber retaining structure and visible supports;
3. rail network entering/leaving the portal;
4. multiple ore carts;
5. crane/winch extraction machinery;
6. forge/workshop and operational support structures;
7. excavated earth/rock integrated into the industrial footprint;
8. lookout/operations tower and storage cues.

It is intentionally distinct from City, Fortress, mountain-only terrain, loose rocks and resource icons.

## Where it is applied

This landmark is intended for HOC2 Living Map territories whose semantic role is `mine`. It replaces generic `rocks`, `mountain`, `cave`, `ore icon` and other fallback readings once promoted into the successor PACK and integrated into runtime.

Gameplay role: extraction/economy territory, mining-resource generation, capture/defense objectives, crafting/build progression and strategic resource routes.

## Forge candidate validation

The PR remains fail-closed until this exact PNG is physically present and passes:

```bash
tehkne-assets-forge validate-hoc-landmark-candidate \
  candidates/hoc/mine-neutral/pack-manifest.json \
  --root candidates/hoc/mine-neutral
```

After structural validation, perform one gameplay-scale review at desktop 1366×768 and portrait 390×844. If it passes, close Mine and proceed to the City+Mine package; do not generate BLUE/RED/DEPLETED variants yet.

## Production state

- composition: complete;
- neutral visual language: complete;
- 2048×2048 runtime normalization: complete;
- checksum/validation metadata: complete;
- physical PNG commit: pending;
- Forge CI against physical binary: pending;
- HOC2 runtime integration: blocked until City+Mine package promotion.

**Tehkné Solutions**
