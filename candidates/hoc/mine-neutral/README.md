# HOC — LANDMARK_MINE_NEUTRAL_01

Status: **CANDIDATE A FROZEN — RUNTIME BINARY MATERIALIZATION ONLY**

This candidate is the production gate for Tehkné Assets Forge issue #7 and Hexa Octarina Conquer #413.

The generated presentation sheet is not an asset and is excluded from production. The isolated Mine render is Candidate A and is frozen: no further Mine generation is allowed unless the HOC gameplay-scale review explicitly rejects this exact asset.

## Identity

- canonical ID: `LANDMARK_MINE_NEUTRAL_01`;
- family: `WORLD_LANDMARKS / EXTRACTION / MINE`;
- application: HOC2 Living Map territories whose semantic role is `mine`;
- gameplay role: extraction/economy territory, resource generation, capture/defense objectives, crafting/build progression and strategic resource routes;
- canonical runtime path: `art/LANDMARK_MINE_NEUTRAL_01.png`.

## Master artistic source

- `2048 × 2048` RGBA PNG;
- SHA-256: `9014411a8c81b89adc3c4ba52b5a3fafd4ad925c7033699c5590e94d36749069`;
- size: `4,524,328 bytes`;
- bottom-center staging with `64 px` bottom/side safety margins;
- neutral stone/timber/iron/earth language with no Blue/Red ownership coding.

The master remains the high-fidelity source artifact and is not regenerated.

## Canonical runtime representation

The same frozen artwork was deterministically optimized for map/runtime delivery without redraw or semantic changes:

- `2048 × 2048` indexed PNG (`P`, 32-color optimized palette);
- SHA-256: `24dbda111549c16d2a3607410a2ed7372d182b592509bc77d1bd390bc9d98b5d`;
- size: `500,338 bytes`;
- fully transparent canvas coverage: `58.3629%`;
- nontransparent bbox (`alpha > 20`): `65,544 → 1983,1984`;
- bottom-center pivot contract preserved;
- visual delta versus the RGBA master at HOC gameplay sizes is small: mean absolute RGBA difference stays approximately `2.58–2.89 / 255` from 64 px through 280 px.

This master/runtime split is intentional: the master preserves source fidelity; the optimized PNG is the version intended for repository/runtime materialization.

## Semantic result

Candidate A reads as a **constructed extraction installation** through:

1. reinforced mine portal embedded in rock;
2. timber retaining structure and visible supports;
3. rail network entering/leaving the portal;
4. multiple ore carts;
5. crane/winch extraction machinery;
6. forge/workshop and operational support structures;
7. excavated earth/rock integrated into the industrial footprint;
8. lookout/operations tower and storage cues.

It is intentionally distinct from City, Fortress, mountain-only terrain, loose rocks and resource icons. It replaces generic `rocks`, `mountain`, `cave` and `ore icon` fallback readings after promotion.

## Permanent Forge gate

`main` contains `HOC Landmark Candidate Gate` (Forge #11 / `802042005a09…`). The candidate must physically contain the exact runtime PNG above, match `SHA256SUMS.txt`, and pass:

```bash
tehkne-assets-forge validate-hoc-landmark-candidate \
  candidates/hoc/mine-neutral/pack-manifest.json \
  --root candidates/hoc/mine-neutral
```

The current red candidate gate is therefore truthful and expected until the exact runtime PNG is committed. Generic CI alone does not count as completion.

After the binary gate passes, perform one gameplay-scale review at desktop `1366×768` and portrait `390×844`. If it passes, close Mine and proceed to the City+Mine package; do not generate BLUE/RED/DEPLETED variants yet.

**Tehkné Solutions**
