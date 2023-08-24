## HDFS_v1
HDFS (http://hadoop.apache.org/hdfs) is the Hadoop Distributed File System designed to run on commodity hardware. Due to the popularity of HDFS, it has been widely studied in the literature. 

This log set is generated in a private cloud environment using benchmark workloads, and manually labeled through handcrafted rules to identify the anomalies. The logs are sliced into traces according to block ids. Then each trace associated with a specific block id is assigned a groundtruth label: normal/anomaly. 

We have preprocessed the dataset for easy use in research, including:
+ HDFS_templates.csv
+ anomaly_label.csv
+ Event_traces.csv
+ Event_occurrence_matrix.csv
+ HDFS.npz

### Download
The raw logs are available for downloading at https://github.com/logpai/loghub.

### Citation
If you use the HDFS_v1 dataset from loghub in your research, please cite the following papers.
+ Wei Xu, Ling Huang, Armando Fox, David Patterson, Michael Jordan. [Detecting Large-Scale System Problems by Mining Console Logs](https://people.eecs.berkeley.edu/~jordan/papers/xu-etal-sosp09.pdf), in Proc. of the 22nd ACM Symposium on Operating Systems Principles (SOSP), 2009.
+ Jieming Zhu, Shilin He, Pinjia He, Jinyang Liu, Michael R. Lyu. [Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics](https://arxiv.org/abs/2008.06448). IEEE International Symposium on Software Reliability Engineering (ISSRE), 2023.


---------------------------------------------------------------------


## HDFS_v2
HDFS (http://hadoop.apache.org/hdfs) is the Hadoop Distributed File System designed to run on commodity hardware. Due to the popularity of HDFS, it has been widely studied in the literature. 

The log set was collected by aggregating logs from the HDFS system in our lab at CUHK for research purpose, which comprises one name node and 32 data nodes. The logs are aggregated at the node level. However, three nodes have been repaired and unfortunately some logs are lost. The logs have a huge size (over 16GB) and are provided as-is without further modification or labelling, which may involve both normal and abnormal cases.

### Download
The raw logs are available for downloading at https://github.com/logpai/loghub.

### Citation
If you use this dataset from loghub in your research, please cite the following papers.
+ Jieming Zhu, Shilin He, Pinjia He, Jinyang Liu, Michael R. Lyu. [Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics](https://arxiv.org/abs/2008.06448). IEEE International Symposium on Software Reliability Engineering (ISSRE), 2023.


---------------------------------------------------------------------


## HDFS_v3_TraceBench
TraceBench is an open data set for trace-oriented monitoring, collected using MTracer on a HDFS system deployed in a real IaaS environment. When collecting, we considered different scenarios, involving multiple scales of clusters, different kinds of user requests, various speeds of workloads, etc. In addition to recording the traces when the HDFS runs normally, we also collected the traces under the situations with various faults injected. There are 17 faults we have injected, including function and performance faults (and real system bugs). The total collection time of TraceBench is more than 180 hours, resulting 364 files that record more than 370,000 traces.

The data are collected through instrumenting the HDFS system. We have converted the raw sql files to csv files and preprocessed the trace logs for easy use in research, including:
+ normal_trace.csv
+ failure_trace.csv
+ eventId.json
+ normal_taskId.json
+ failure_taskId.json

For more detailed information, please visit the dataset project: https://mtracer.github.io/TraceBench.

### Download
The raw logs are available for downloading at https://github.com/logpai/loghub.

### Citation
If you use this dataset from loghub in your research, please cite the following paper.
+ Jingwen Zhou, Zhenbang Chen, Ji Wang, Zibin Zheng, and Michael R. Lyu. [TraceBench: An Open Data Set for Trace-oriented Monitoring](http://zbchen.github.io/Papers_files/cloudcom2014.pdf), in Proceedings of the 6th IEEE International Conference on Cloud Computing Technology and Science (CloudCom), 2014.
+ Jieming Zhu, Shilin He, Pinjia He, Jinyang Liu, Michael R. Lyu. [Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics](https://arxiv.org/abs/2008.06448). IEEE International Symposium on Software Reliability Engineering (ISSRE), 2023.

