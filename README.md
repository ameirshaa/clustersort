Readme
====================
This code runs together with the code from fast cluster analysis which is provided by Tom Whyntie et al. 

Instructions
---------------------

Things you will need: CERNVM, Python Libraries: matplotlib, PIL, numpy, collections

CERNVM can be downloaded from here: https://cernvm.cern.ch/portal/downloads 

Alternatively (instead of downloading all the above mentioned libraries) you can download Anaconda 2.7 from here: https://www.continuum.io/downloads

### How to use

* Create an empty data folder to store all the raw data from the Timepix detector
* Create an empty tmp folder to store all the information being processed

* To create the clusters: 

```bash
$ python process-frames.py data tmp
```

* To run the sorting algorithm:

```bash
$ python usepixeldata.py
```

* (Optional) To create graphs showing information about ALL the clusters:

```bash
$ python make-plots.py tmp tmp
```

* You will see a graph containing the information of the sorted clusters. 
