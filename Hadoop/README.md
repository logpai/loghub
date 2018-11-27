## Hadoop
Hadoop (https://hadoop.apache.org) is a big data processing framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. Due to the increasing importance of Hadoop in industry, it has been widely studied in the literature. 

The logs are generated from a Hadoop cluster with 46 cores across five machines. Each machine has Intel(R) Core(TM) i7-3770 CPU and 16GB RAM. Two testing applications are executed:
+ *WordCount*: an application that is released with Hadoop as an example of MapReduce programming. The WordCount application analyzes the input files and counts the number of
occurrences of each word in the input files.
+ *PageRank*: a program that is used by a search engine for ranking Web pages. 

Firstly, the applications are run without injecting any failure. Then, in order to simulate service failures in the production environment, the following deployment failures are injected:
+ *Machine down*: turn off one server when the applications are running to simulate the machine failure.
+ *Network disconnection*: disconnect one server from the network to simulate the network connection failure.
+ *Disk full*: manually fill up one server's hard disk when the applications are running to simulate the disk full failure.

You may find more details of this dataset from the original paper:
+ Qingwei Lin, Hongyu Zhang, Jian-Guang Lou, Yu Zhang, Xuewei Chen. [Log Clustering Based Problem Identification for Online Service Systems](http://ieeexplore.ieee.org/document/7883294/), in Proc. of International Conference on Software Engineering (ICSE), 2016. 

Note that `Hadoop_2k.log` is a sample log. The raw logs can be requested from Zenodo: https://doi.org/10.5281/zenodo.1144100




