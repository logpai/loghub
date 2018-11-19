## HDFS
HDFS (http://hadoop.apache.org/hdfs) is the Hadoop Distributed File System designed to run on commodity hardware. Due to the popularity of HDFS, it has been widely studied in recent years. We provide two sets of HDFS logs in loghub.

Note that `HDFS_2k.log` is a sample log. The raw logs can be requested from Zenodo: https://doi.org/10.5281/zenodo.1144100

### HDFS_1
The [log set](http://iiis.tsinghua.edu.cn/~weixu/sospdata.html) is generated in a private cloud environment using benchmark workloads, and manually labeled through handcrafted rules to identify the anomalies. The logs are sliced into traces according to block ids. Then each trace associated with a specific block id is assigned a groundtruth label: normal/anomaly. You may find more details of this dataset from the original paper:

+ Wei Xu, Ling Huang, Armando Fox, David Patterson, Michael Jordan. [Large-scale System Problem Detection by Mining Console Logs](http://iiis.tsinghua.edu.cn/~weixu/files/sosp09.pdf), In Proc. of the 22nd ACM Symposium on Operating Systems Principles (SOSP), 2009.

### HDFS_2
The log set was collected by aggregating logs from the HDFS system in our lab at CUHK for research purpose, which comprises one name node and 32 data nodes. The logs are aggregated at the node level. However, three nodes have been repaired and unfortunately some logs are lost. The logs have a huge size (over 16GB) and are provided as-is without further modification or labelling, which may involve both normal and abnormal cases. 




