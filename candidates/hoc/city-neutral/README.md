# HOC — LANDMARK_CITY_NEUTRAL_01

Status: **CANDIDATE A FROZEN — NEUTRAL BINARY MATERIALIZATION ONLY**

This candidate is the production gate for Tehkné Assets Forge issue #6 and Hexa Octarina Conquer #413.

The exploration/concept sheets are references only. Candidate A is frozen: no further City generation is allowed unless the HOC gameplay-scale review explicitly rejects this exact asset.

## Canonical Candidate A

- canonical ID: `LANDMARK_CITY_NEUTRAL_01`;
- canonical path: `art/LANDMARK_CITY_NEUTRAL_01.png`;
- normalized canvas: `2048 × 2048` RGBA;
- fully transparent canvas coverage: `61.9939%`;
- nontransparent bbox (`alpha > 20`): `64,673 → 1984,1984`;
- bottom margin: `64 px`;
- pivot contract: bottom-center;
- exact neutral PNG SHA-256: `18f4b6df860fcfe46f37e7c51ee8f1c03ea6de2a9ed37ad83de222deb8bb881b`;
- exact neutral PNG size: `4,052,562 bytes`;
- no baked board text, UI, badge, marker, frame, logo or HUD treatment;
- no Blue/Red faction coding in roofs, banners or standards;
- broad inhabited footprint with civic center, multiple homes/workshops, market, farm, windmill and streets;
- semantic review: reads as population/economy/civilization rather than a single fortress, tower or camp.

## Forge candidate validation

The frozen Candidate A package is expected to pass the fail-closed candidate contract once the exact binary is physically present:

```bash
tehkne-assets-forge validate-hoc-landmark-candidate \
  candidates/hoc/city-neutral/pack-manifest.json \
  --root candidates/hoc/city-neutral
```

## Permanent binary gate

`main` now contains `HOC Landmark Candidate Gate` (Forge #11 / `802042005a09…`). Any PR touching `candidates/hoc/**` must physically contain its canonical asset, match `SHA256SUMS.txt`, and pass `validate-hoc-landmark-candidate`. A generic green CI no longer counts as candidate completion.

## Remaining gate

The exact neutral binary has been produced and preserved outside the repository. The PR remains fail-closed until that exact PNG is physically committed to `art/LANDMARK_CITY_NEUTRAL_01.png` and the permanent binary gate validates the file against the checksum above.

This is a **binary materialization blocker only**. Do not generate another City, do not start BLUE/RED/DAMAGED variants, and do not integrate City into HOC runtime before that gate is satisfied.

**Tehkné Solutions**
