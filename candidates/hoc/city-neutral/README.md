# HOC — LANDMARK_CITY_NEUTRAL_01

Status: **CANDIDATE A LOCALLY VALIDATED — BINARY MATERIALIZATION PENDING**

This candidate is the production gate for Tehkné Assets Forge issue #6 and Hexa Octarina Conquer #413.

The concept sheets generated during exploration are references only. They are not canonical runtime assets because they contain presentation boards, labels, surrounding scene context and/or non-runtime composition.

## Candidate A

A dedicated isolated City render has now been produced and normalized for runtime review.

- canonical ID: `LANDMARK_CITY_NEUTRAL_01`;
- normalized canvas: `2048 × 2048` RGBA;
- transparent canvas coverage: `71.17%` fully/nearly transparent;
- authored image SHA-256: `ccca55b46341f60f8c33620a179dc8c0188e07d05d1bf0da8fd5ae1ddfbe0ee2`;
- bottom-center staging preserved for world-space pivoting;
- no baked board text, UI, badge, marker, frame, logo or HUD treatment;
- broad inhabited footprint with civic center, multiple homes/workshops, market, farm, windmill and streets;
- human scale review: strong at ~140–220 px, readable as a compact city at ~96 px, silhouette remains distinct at ~64 px;
- semantic review: reads as population/economy/civilization rather than a single fortress, tower or camp.

## Forge candidate validation

Using the current `main` implementation of `validate_hoc_landmark_candidate`, a local package containing Candidate A and this manifest returned:

```json
{
  "valid": true,
  "mode": "candidate",
  "schema": "hoc/world-landmarks/v1",
  "project": "Hexa Octarina Conquer",
  "asset_count": 1,
  "asset_id": "LANDMARK_CITY_NEUTRAL_01",
  "signature": "Tehkné Solutions"
}
```

The canonical command remains:

```bash
tehkne-assets-forge validate-hoc-landmark-candidate \
  candidates/hoc/city-neutral/pack-manifest.json \
  --root candidates/hoc/city-neutral
```

## Remaining gate

The connected GitHub contents workflow used in this session does not provide direct binary-file materialization from the generated local PNG. Therefore the PR remains fail-closed until `art/LANDMARK_CITY_NEUTRAL_01.png` is physically committed to this branch and the same candidate gate runs in CI against that exact file.

No BLUE/RED/DAMAGED variants and no HOC runtime integration should proceed before that binary-materialization gate is satisfied.

**Tehkné Solutions**
