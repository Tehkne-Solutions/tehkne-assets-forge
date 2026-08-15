# HOC — LANDMARK_CITY_NEUTRAL_01

Status: **CANDIDATE A FROZEN — BINARY MATERIALIZATION ONLY**

This candidate is the production gate for Tehkné Assets Forge issue #6 and Hexa Octarina Conquer #413.

The exploration/concept sheets are references only. Candidate A is now frozen: no further City generation is allowed unless the HOC gameplay-scale review explicitly rejects this exact asset.

## Canonical Candidate A

- canonical ID: `LANDMARK_CITY_NEUTRAL_01`;
- canonical path: `art/LANDMARK_CITY_NEUTRAL_01.png`;
- normalized canvas: `2048 × 2048` RGBA;
- fully transparent canvas coverage: `61.9939%`;
- nontransparent bbox (`alpha > 20`): `64,673 → 1984,1984`;
- bottom margin: `64 px`;
- pivot contract: bottom-center;
- exact PNG SHA-256: `5af95fbb0fe03ab722c4267b37cf675cf9f9a5d9b0be41bf881e736aa9c37cdc`;
- exact PNG size: `4,037,330 bytes`;
- no baked board text, UI, badge, marker, frame, logo or HUD treatment;
- broad inhabited footprint with civic center, multiple homes/workshops, market, farm, windmill and streets;
- semantic review: reads as population/economy/civilization rather than a single fortress, tower or camp.

## Forge candidate validation

The frozen Candidate A package passes the same fail-closed contract implemented on `main`:

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

Canonical command:

```bash
tehkne-assets-forge validate-hoc-landmark-candidate \
  candidates/hoc/city-neutral/pack-manifest.json \
  --root candidates/hoc/city-neutral
```

## Remaining gate

The generated binary exists and is frozen, but the connected GitHub tool available in this session does not expose a local-file binary upload parameter. The PR therefore remains fail-closed until the exact PNG above is physically committed to `art/LANDMARK_CITY_NEUTRAL_01.png` and CI validates that exact SHA.

This is a **binary materialization blocker only**. Do not generate another City, do not start BLUE/RED/DAMAGED variants, and do not integrate City into HOC runtime before that gate is satisfied.

**Tehkné Solutions**
