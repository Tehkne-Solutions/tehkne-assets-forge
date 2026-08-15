# HOC — LANDMARK_CITY_NEUTRAL_01

Status: **ART CANDIDATE REQUIRED**

This candidate is the production gate for Tehkné Assets Forge issue #6 and Hexa Octarina Conquer #413.

The concept sheets generated during exploration are references only. They are not canonical runtime assets because they contain presentation boards, labels, surrounding water/scene context and/or non-transparent backgrounds.

## Required final render

- exact canonical ID: `LANDMARK_CITY_NEUTRAL_01`;
- isolated world-space city/settlement render;
- transparent background;
- no baked text, UI, badge, marker, frame, logo or HUD treatment;
- broad inhabited footprint with multiple architectural masses rather than a single fortress/tower silhouette;
- readable at HOC Living Map gameplay scale;
- neutral materials and identity before BLUE/RED/DAMAGED variants;
- preserve the visual production contract on `main`.

## Validation

Once `art/LANDMARK_CITY_NEUTRAL_01.png` exists, run:

```bash
tehkne-assets-forge validate-hoc-landmark-candidate \
  candidates/hoc/city-neutral/pack-manifest.json \
  --root candidates/hoc/city-neutral
```

The branch must remain fail-closed until the actual PNG exists and passes human review.

**Tehkné Solutions**
