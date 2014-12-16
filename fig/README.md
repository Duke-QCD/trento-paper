# Figures

The Python script `make-plots` generates all figures.
Relatively recent versions of numpy and matplotlib are required.

The data files for the figures are too large to be tracked in git (total compressed size ~310 MiB).
Instead, an archive containing the data is publicly available at http://phy.duke.edu/~jeb65/trento-fig-data.tar.gz.
Run the included script `./download-data` to download the archive, verify its integrity, and extract it.

After acquiring the data, run `./make-plots`.

## Auxiliary parameters

### Cross sections

√s [GeV] | σ<sub>NN</sub> [mb]
-------- | -------------------
200      | 42.0
2360     | 62.9
2760     | 64.0
5020     | 71.0

### Woods-Saxon parameters

- R: nuclear radius
- d: surface thickness
- β<sub>n</sub>: angular deformation parameters

Nucleus | R [fm] | d [fm] | β<sub>2</sub> | β<sub>4</sub>
------- | ------ | ------ | ------------- | -------------
<sup>197</sup>Au | 6.38 | 0.535 | 0     | 0
<sup>208</sup>Pb | 6.62 | 0.546 | 0     | 0
<sup>238</sup>U  | 6.81 | 0.605 | 0.286 | 0.093
