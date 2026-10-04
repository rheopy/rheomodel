# rheomodel — rheological constitutive models

[![CI](https://github.com/rheopy/rheomodel/actions/workflows/ci.yml/badge.svg)](https://github.com/rheopy/rheomodel/actions/workflows/ci.yml)
[![Documentation Status](https://readthedocs.org/projects/rheomodel/badge/?version=latest)](https://rheomodel.readthedocs.io/en/latest/)

Nine flow-curve models as pure Python functions — equations, parameters,
bounds, and **verified academic citations**. No fitting machinery: that lives
in [rheofit](https://github.com/rheopy/rheofit), which consumes these models.

```python
pip install rheopy-rheomodel
```

```python
import numpy as np
import rheomodel

hb = rheomodel.get_model("herschel_bulkley")
gd = np.logspace(-3, 3, 100)
sigma = hb.equation(gd, sigma_y=20.0, K=10.0, n=0.6)
```

Each model carries its provenance: `CITATION` (authors, journal, DOI — every
DOI verified to resolve), `PARAM_INFO` (symbols, units, descriptions),
`get_equation_latex()`, and the model ladder (`PARENT` / `PARENT_EXACT`).

The [model guides](https://github.com/rheopy/rheomodel/tree/master/docs/models)
cover each model's history, physics, applicable materials, and limitations,
with interactive in-browser explorers.

## Models

| Family | Models |
|---|---|
| Yield stress | `herschel_bulkley`, `bingham`, `casson` |
| Microstructure-informed (MIRM) | `tc`, `tc_carreau`, `tccc` |
| No yield stress | `power_law`, `carreau`, `carreau_carreau` |

## Part of rheopy

[rheopy](https://github.com/rheopy) bundles know-how end to end: measure →
data ([rheodata](https://github.com/rheopy/rheodata)) → models (here) →
fitting ([rheofit](https://github.com/rheopy/rheofit)) → in-browser
playground ([rheolite](https://github.com/rheopy/rheolite)).

## License

MIT
