# HOC — LANDMARK_MINE_NEUTRAL_01

Status: **FAIL-CLOSED PRODUCTION GATE — ASSET NOT MATERIALIZED**

This candidate is the production gate for Tehkné Assets Forge issue #7 and Hexa Octarina Conquer #413.

## Canonical output

- canonical ID: `LANDMARK_MINE_NEUTRAL_01`;
- canonical path: `art/LANDMARK_MINE_NEUTRAL_01.png`;
- isolated world-space PNG with transparent background;
- neutral stone/timber/iron/earth palette;
- no baked text, UI, marker, badge, frame or faction coding;
- bottom-center pivot staging;
- authored silhouette must remain legible at HOC gameplay scale.

## Locked semantic contract

The Mine must read as a **constructed extraction site**, not as a mountain, rock pile or resource icon.

Required authored cues:

1. dark mine portal embedded in excavated terrain;
2. timber/stone retaining structure around the portal;
3. visible support beams;
4. short rail/cart track or extraction path leaving the entrance;
5. winch, pulley, crane or ore-cart extraction cue;
6. excavated rock/earth footprint integrated into the installation;
7. enough asymmetry and industrial construction to remain distinct from Fortress and City.

Forbidden readings:

- loose rocks only;
- generic cave hole;
- mountain-only silhouette;
- ore/resource icon;
- house, city or fortress;
- Blue/Red ownership colors;
- UI icon/card/marker.

## Candidate gate

The PR must remain fail-closed until the exact PNG exists and passes:

```bash
tehkne-assets-forge validate-hoc-landmark-candidate \
  candidates/hoc/mine-neutral/pack-manifest.json \
  --root candidates/hoc/mine-neutral
```

After structural validation, perform one gameplay-scale review at desktop 1366×768 and portrait 390×844. If it passes, freeze the candidate; do not generate iterative concept sheets or faction variants before approval.

The final City+Mine package remains blocked until both neutral candidates are physically materialized and individually approved.

**Tehkné Solutions**
