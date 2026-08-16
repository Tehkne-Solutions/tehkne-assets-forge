# HOC — LANDMARK_CITY_NEUTRAL_01

Status: **CANDIDATE A FROZEN — RUNTIME MATERIALIZED**

This candidate is the production gate for Tehkné Assets Forge issue #6 and Hexa Octarina Conquer #413.

The exploration/concept sheets are references only. Candidate A is frozen: no further City generation is allowed unless the HOC gameplay-scale review explicitly rejects this exact asset.

## Identity

- canonical ID: `LANDMARK_CITY_NEUTRAL_01`;
- family: `WORLD_LANDMARKS / SETTLEMENT / CITY`;
- application: HOC2 Living Map territories whose semantic role is `city`;
- gameplay role: population/economy/civilization territory, settlement objectives, strategic occupation and future ownership-state presentation;
- canonical runtime path: `art/LANDMARK_CITY_NEUTRAL_01.png`.

## Master artistic source

- `2048 × 2048` RGBA PNG;
- SHA-256: `18f4b6df860fcfe46f37e7c51ee8f1c03ea6de2a9ed37ad83de222deb8bb881b`;
- size: `4,052,562 bytes`;
- bottom-center staging with `64 px` bottom safety margin;
- no Blue/Red faction coding in roofs, banners or standards;
- broad inhabited footprint with civic center, clustered homes/workshops, market, farm, windmill and streets.

The master remains the high-fidelity source artifact and is not regenerated.

## Canonical runtime representation

The same frozen artwork is deterministically optimized for map delivery and is physically materialized in this PR:

- `384 × 384` indexed PNG (`P`, 64-color optimized palette);
- SHA-256: `9c0b521e0ee001a307c051d33540aa73022d91561ce5aadbe7a6b0acfdbf2dd3`;
- size: `30,503 bytes`;
- bottom-center composition preserved;
- current `LivingMap` presents authored landmark art at `96 × 96`, so this runtime retains exactly 4× source-resolution headroom;
- mean absolute visual delta versus the RGBA master remains approximately `2.22–3.30 / 255` across 64–220 px review sizes.

This master/runtime split is intentional: source fidelity remains in the 2048px master; the repository and game ship the appropriately sized runtime asset.

## Semantic result

Candidate A reads as **population / economy / civilization** through multiple inhabited masses, civic center, market, productive structures and street logic. It is intentionally distinct from Fortress, tower, camp and Mine.

After promotion it replaces generic or misleading City fallbacks in HOC2 Living Map territories.

## Permanent Forge gate

`main` contains `HOC Landmark Candidate Gate` (Forge #11 / `802042005a09…`). This PR physically contains the runtime PNG and `SHA256SUMS.txt` is locked to its exact bytes. The permanent gate must pass:

```bash
tehkne-assets-forge validate-hoc-landmark-candidate \
  candidates/hoc/city-neutral/pack-manifest.json \
  --root candidates/hoc/city-neutral
```

After the binary gate passes, perform one gameplay-scale review at desktop `1366×768` and portrait `390×844`. If it passes, close City and proceed to the City+Mine package; do not generate BLUE/RED/DAMAGED variants yet.

**Tehkné Solutions**
