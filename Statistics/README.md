# FYS5555 Statistics

Prepared by Magnar Bugge

This section allows the computation of "cut-and-count" ("single-bin") cross section limits on a new signal
process and production of standard limit plots including bands for the 1- and 2-sigma variations of the
limit around the expected (median) value.

Inputs are read from the file "inputs.txt", which is currently set up to reproduce the electron channel
limits (Fig. 2, top left) from https://arxiv.org/abs/1407.7494. The format is

```
[Number of mass points]
[W' mass] [mT threshold]
[signal efficiency] [signal eff. uncertainty] [number of predicted signal events] [background] [background uncertainty] [observed data]
[W' mass] [mT threshold]
[signal efficiency] [signal eff. uncertainty] [number of predicted signal events] [background] [background uncertainty] [observed data]
[W' mass] [mT threshold]
[signal efficiency] [signal eff. uncertainty] [number of predicted signal events] [background] [background uncertainty] [observed data]
...
...
...
```

The plot from the above publication can be reproduced with the commands:
- `root -l -q runLimits.cpp`
- `root -l limitPlot.cpp`

The code depends on ROOT (which you have already installed in your Anaconda environment).

## Combining channels

A corresponding script is also provided for running limit calculations that combine the information in two
or more channels. Example inputs for running combined limits for the electron and muon channels in the example
publication above are in the file "inputs_bothChannels.txt", with the structure:
```
[Number of mass points] [Number of channels]
[W' mass] [mT threshold]
[signal efficiency channel 1] [signal eff. uncertainty channel 1] ...
[signal efficiency channel 2] [signal eff. uncertainty channel 2] ...
...
...
[W' mass] [mT threshold]
[signal efficiency channel 1] [signal eff. uncertainty channel 1] ...
[signal efficiency channel 2] [signal eff. uncertainty channel 2] ...
...
...
...
```
A combined limit plot, corresponding to the lower left plot in Fig. 2 of the above publication, is created with
the commands:
- `root -l -q runLimits_combined.cpp`
- `root -l limitPlot.cpp`

Note that the limit calculations in this case can take considerably longer, and the accuracy parameters in the
script "runLimits_combined.cpp" are tuned to give a relatively nice plot in about 2.5 hours for the example inputs.
Note that the plot produced with the above commands will not be exactly identical to the one in the publication,
as the division of systematic uncertainties into components that are treated respectively as correlated and uncorrelated
between the channels is beyond the scope of the current setup.
