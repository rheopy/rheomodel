# rheomodel

**Rheological constitutive models, with the science attached.** Nine flow-curve
models — equations, parameters, verified academic citations, and the
microstructure-informed (MIRM) combinations — as pure, dependency-light Python
functions. Fitting machinery lives in [rheofit](https://github.com/rheopy/rheofit);
data lives in [rheodata](https://github.com/rheopy/rheodata).

```python
import numpy as np
import rheomodel

hb = rheomodel.get_model("herschel_bulkley")
gd = np.logspace(-3, 3, 100)
sigma = hb.equation(gd, sigma_y=20.0, K=10.0, n=0.6)
print(hb.CITATION["doi"])  # 10.1007/BF01432034
```

## Models

```{toctree}
:maxdepth: 1

models/index
```

## API reference

```{toctree}
:maxdepth: 1

api
```

## Part of rheopy

rheomodel is one piece of the [rheopy](https://github.com/rheopy) bundle:
**measure** the data → **rheodata** shares it → **rheomodel** explains it →
**rheofit** fits it → **rheolite** runs it all in your browser.
