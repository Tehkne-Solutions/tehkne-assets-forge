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

The same frozen artwork is deterministically optimized for map delivery:

- `512 × 512` indexed PNG (`P`, 64-color optimized palette);
- SHA-256: `4398f8d96c1bfb50d89a34717f4ce18a5ad69140864dec99eb814d7e3d9b00c4`;
- size: `48,099 bytes`;
- bottom-center composition preserved;
- current `LivingMap` displays landmark art at `96 × 96`, so this runtime retains more than 5× source resolution headroom;
- mean absolute visual delta versus the RGBA master remains approximately `2.46–3.07 / 255` across 64–220 px review sizes.

This master/runtime split is intentional: source fidelity remains in the 2048px master; the repository and game ship the appropriately sized runtime asset.

## Semantic result

Candidate A reads as a **constructed extraction installation** through reinforced portal, timber supports, rail network, ore carts, crane/winch machinery, forge/workshop, operations tower, storage and excavated terrain. It is intentionally distinct from City, Fortress, mountain-only terrain, loose rocks and resource icons.

After promotion it replaces generic `rocks`, `mountain`, `cave` and `ore icon` fallback readings for Mine territories.

## Permanent Forge gate

`main` contains `HOC Landmark Candidate Gate` (Forge #11 / `802042005a09…`). The candidate must physically contain the exact runtime PNG above, match `SHA256SUMS.txt`, and pass:

```bash
tehkne-assets-forge validate-hoc-landmark-candidate \
  candidates/hoc/mine-neutral/pack-manifest.json \
  --root candidates/hoc/mine-neutral
```

The current red candidate gate is truthful and expected until the exact runtime PNG is committed. Generic CI alone does not count as completion.

After the binary gate passes, perform one gameplay-scale review at desktop `1366×768` and portrait `390×844`. If it passes, close Mine and proceed to the City+Mine package; do not generate BLUE/RED/DEPLETED variants yet.

**Tehkné Solutions**
