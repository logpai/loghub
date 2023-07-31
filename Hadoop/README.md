## Hadoop
Hadoop (https://hadoop.apache.org) is a big data processing framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. Due to the increasing importance of Hadoop in industry, it has been widely studied in the literature. 

The logs are generated from a Hadoop cluster with 46 cores across five machines. Each machine has Intel(R) Core(TM) i7-3770 CPU and 16GB RAM. Specifically, two testing applications are executed:
+ *WordCount*: an application that is released with Hadoop as an example of MapReduce programming. The WordCount application analyzes the input files and counts the number of occurrences of each word in the input files.
+ *PageRank*: a program that is used by a search engine for ranking Web pages. 

Each application has been run for several times, simulating both normal and abnormal cases with injected specific failures. Firstly, the applications are run without injecting any failure. Then, in order to simulate service failures in the production environment, the following deployment failures are injected:
+ *Machine down*: turn off one server when the applications are running to simulate the machine failure.
+ *Network disconnection*: disconnect one server from the network to simulate the network connection failure.
+ *Disk full*: manually fill up one server's hard disk when the applications are running to simulate the disk full failure.

We provide the labeled abnormal/normal job IDs in `abnormal_label.txt`.

### Download
The raw logs are available for downloading at https://github.com/logpai/loghub.

### Citation
If you use this dataset from loghub in your research, please cite the following paper.
+ Qingwei Lin, Hongyu Zhang, Jian-Guang Lou, Yu Zhang, Xuewei Chen. [Log Clustering Based Problem Identification for Online Service Systems](http://ieeexplore.ieee.org/document/7883294/), International Conference on Software Engineering (ICSE), 2016.
+ Jieming Zhu, Shilin He, Pinjia He, Jinyang Liu, Michael R. Lyu. [Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics](https://arxiv.org/abs/2008.06448). IEEE International Symposium on Software Reliability Engineering (ISSRE), 2023.
