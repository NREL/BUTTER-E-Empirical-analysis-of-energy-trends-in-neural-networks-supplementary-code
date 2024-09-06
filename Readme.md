# Codebase for Measuring the Energy Consumption and Efficiency of Deep Neural Networks: An Empirical Analysis and Design Recommendations

This codebase contains the notebooks and code to generate the BUTTER-E Dataset artifacts and figures as described in the publication *Measuring the Energy Consumption and Efficiency of Deep Neural Networks: An Empirical Analysis and Design Recommendations*.

- **Publication**: [Arxiv Link](https://arxiv.org/abs/2403.08151)
- **Dataset**: See the [Data Readme](Readme%20for%20Data.md) for more information. Data is hosted here: [OEDI Butter-E 5991](https://data.openei.org/submissions/5991).

The dataset was generated using our BUTTER Empirical Deep Learning Experimental Framework - [DOE Code record](https://www.osti.gov/doecode/biblio/74457), [Github Repository](https://github.com/NREL/BUTTER-Empirical-Deep-Learning-Experimental-Framework)

## How To Cite This Work

> Tripp, C. E., Perr-Sauer, J., Gafur, J., Nag, A., Purkayastha, A., Zisman, S., & Bensen, E. A. (2024). Measuring the Energy Consumption and Efficiency of Deep Neural Networks: An Empirical Analysis and Design Recommendations (arXiv:2403.08151). arXiv. http://arxiv.org/abs/2403.08151


## Quickstart

### 1. Download the Data Set

- All of the data inputs must be placed in the `./data_inputs` directory. A list of these datasets, and download links, are located in [Readme for Data.md](Readme%20for%20Data.md)
- Extract any of the datasets which are compressed in that directory.


### 2. Set Up Environment

This codebase should run inside of the Microsoft Anaconda Docker Image, or any complete Anaconda environment (Python 3.9) wihthout modification.
For completeness, we have exported a frozen Anaconda environment.yml file to the root of this repository.

```
docker pull mcr.microsoft.com/devcontainers/anaconda:0-3
```

### 3. Open and run the notebooks

Make sure to run the notebooks in order, as data generated in previous notebooks is loaded by subsequent notebooks.

```
jupyter notebook
```

## Acknowledgements

Released under software record NREL/SWR-23-70. *Empirical analysis of energy trends in neural networks supplementary code. Erik Bensen, Charles Tripp, Ambarish Nag, Sagi Zisman, Jordan Perr-Sauer, Jamil Gafur.*
