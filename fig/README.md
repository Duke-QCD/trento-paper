# Figures

The Python scripts `data/trento/generate-events-{lhc,rhic}` generate event data for plotting.
Run them, then run `make-plots` to create the figures.
Relatively recent versions of numpy and matplotlib are required.

## Auxiliary parameters

### Cross sections

√s [GeV] | σ<sub>NN</sub> [mb]
-------- | -------------------
200      | 42
2360     | 63
2760     | 64
5020     | 71

### Woods-Saxon parameters

- R: nuclear radius
- d: surface thickness
- β<sub>n</sub>: angular deformation parameters

Nucleus | R [fm] | d [fm] | β<sub>2</sub> | β<sub>4</sub>
------- | ------ | ------ | ------------- | -------------
<sup>197</sup>Au | 6.38 | 0.535 | 0    | 0
<sup>208</sup>Pb | 6.62 | 0.546 | 0    | 0
<sup>238</sup>U  | 6.67 | 0.44  | 0.28 | 0.093
