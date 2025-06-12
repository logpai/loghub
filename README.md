<p align="center"> <a href="https://github.com/logpai"> <img src="https://cdn.jsdelivr.net/gh/logpai/logpai.github.io@master/img/logpai_logo.jpg" width="480"></a></p>


<div>
<a href="https://github.com/logpai/loghub/stargazers"><img src="http://bytecrank.com/nastyox/reporoster/php/stargazersSVG.php?user=logpai&repo=loghub" width="600"/><a/>
</div>

# Loghub

Loghub maintains a collection of system logs, which are freely accessible for AI-driven log analytics research. Some of the logs are production data released from previous studies, while some others are collected from real systems in our lab environment. Wherever possible, the logs are NOT sanitized, anonymized or modified in any way. These log datasets are freely available for research or academic work.

🤗 We proudly announce that the loghub datasets have attained total <a href="https://doi.org/10.5281/zenodo.1144100"><img src="https://img.shields.io/endpoint?&url=https://cdn.jsdelivr.net/gh/logpai/loghub@zenodo/downloads.json&labelColor=1AE&color=DDEEFF&style=flat&label=Downloads"></a> by more than [**450 organizations**](https://github.com/logpai/loghub/wiki/Loghub-download-list) from both industry and academia.

### Logs currently available

🔗 Get raw logs via hyperlinks in the Download column.

| Dataset              | Description | Labeled | Time Span  |  #Lines  |   Raw Size   |  Download  |
| :---------------------------- | :--------|  :--------: | --------: | ---------: | ------: | :------: | 
|<tr><th colspan=7 align="center">:open_file_folder: **Distributed systems**</th></tr>|
| [HDFS_v1](./HDFS#hdfs_v1)     | Hadoop distributed file system log | :heavy_check_mark: | 38.7 hours | 11,175,629  |  1.47GiB  | [:link:](https://zenodo.org/records/8196385/files/HDFS_v1.zip?download=1)   |      
| [HDFS_v2](./HDFS#hdfs_v2)     | Hadoop distributed file system log|  |    N.A.    | 71,118,073  | 16.06GiB  | [:link:](https://zenodo.org/records/8196385/files/HDFS_v2.zip?download=1)  |
| [HDFS_v3](./HDFS#hdfs_v3_tracebench)     | Instrumented HDFS trace log (TraceBench) | :heavy_check_mark: |    N.A.    | 14,778,079  | 2.96GiB  | [:link:](https://zenodo.org/records/8196385/files/HDFS_v3_TraceBench.zip?download=1)  |
| [Hadoop](./Hadoop)            |  Hadoop mapreduce job log | :heavy_check_mark: (Check [#56](https://github.com/logpai/loghub/issues/56)) |   N.A.    |   394,308   | 48.61MiB  |  [:link:](https://zenodo.org/records/8196385/files/Hadoop.zip?download=1)  |
| [Spark](./Spark)              | Spark job log ||    N.A.    | 33,236,604  |  2.75GiB  | [:link:](https://zenodo.org/records/8196385/files/Spark.tar.gz?download=1)  |                            
| [Zookeeper](./Zookeeper)      | ZooKeeper service log | | 26.7 days  |   74,380    | 9.95MiB  |  [:link:](https://zenodo.org/records/8196385/files/Zookeeper.tar.gz?download=1)   | 
| [OpenStack](./OpenStack)      |  OpenStack infrastructure log | :heavy_check_mark: |  N.A.    |   207,820   | 58.61MiB  |  [:link:](https://zenodo.org/records/8196385/files/OpenStack.tar.gz?download=1)  |    
|<tr><th colspan=7 align="center">:open_file_folder: **Super computers**</th></tr>|
| [BGL](./BGL)          | Blue Gene/L supercomputer log | :heavy_check_mark: | 214.7 days |  4,747,963  | 708.76MiB |  [:link:](https://zenodo.org/records/8196385/files/BGL.zip?download=1)   |
| [HPC](./HPC)                  |  High performance cluster log | |  N.A.    |   433,489   | 32.00MiB  |  [:link:](https://zenodo.org/records/8196385/files/HPC.zip?download=1)  |           
| [Thunderbird](./Thunderbird)  |  Thunderbird supercomputer log | :heavy_check_mark: | 244 days  | 211,212,192 | 29.60GiB  | [:link:](https://zenodo.org/records/8196385/files/Thunderbird.tar.gz?download=1)  |
|<tr><th colspan=7 align="center">:open_file_folder: **Operating systems**</th></tr>|  
| [Windows](./Windows)          | Windows event log | | 226.7 days | 114,608,388 | 26.09GiB  | [:link:](https://zenodo.org/records/8196385/files/Windows.tar.gz?download=1)   |    
| [Linux](./Linux)              | Linux system log | | 263.9 days |   25,567    |  2.25MiB  |  [:link:](https://zenodo.org/records/8196385/files/Linux.tar.gz?download=1)  |
| [Mac](./Mac)                  | Mac OS log | | 7.0 days  |   117,283   | 16.09MiB  | [:link:](https://zenodo.org/records/8196385/files/Mac.tar.gz?download=1)  |
|<tr><th colspan=7 align="center">:open_file_folder: **Mobile systems**</th></tr>|  
| [Android_v1](./Android#android_v1)          |  Android framework log | |  N.A.    | 1,555,005  |  183.37MiB | [:link:](https://zenodo.org/records/8196385/files/Android_v1.zip?download=1) |
| [Android_v2](./Android#android_v2)          |  Android framework log | |  N.A.    | 30,348,042  | 3.38GiB  | [:link:](https://zenodo.org/records/8196385/files/Android_v2.zip?download=1)  |
| [HealthApp](./HealthApp)      | Health app log  | | 10.5 days  |   253,395   | 22.44MiB  | [:link:](https://zenodo.org/records/8196385/files/HealthApp.tar.gz?download=1)  |
|<tr><th colspan=7 align="center">:open_file_folder: **Server applications**</th></tr>|            
| [Apache](./Apache) | Apache web server error log | | 263.9 days |   56,481    |  4.90MiB  | [:link:](https://zenodo.org/records/8196385/files/Apache.tar.gz?download=1)   |                     
| [OpenSSH](./OpenSSH)          | OpenSSH server log | | 28.4 days  |   655,146   | 70.02MiB  | [:link:](https://zenodo.org/records/8196385/files/SSH.tar.gz?download=1) |
|<tr><th colspan=7 align="center">:open_file_folder: **Standalone software**</th></tr>|                           
| [Proxifier](./Proxifier)      |   Proxifier software log | | N.A.    |   21,329    |  2.42MiB  |   [:link:](https://zenodo.org/records/8196385/files/Proxifier.tar.gz?download=1) |                                           


### 🔥 Citation

Please cite the following two papers if you use the loghub datasets in your research.

+ **Loghub**: Jieming Zhu, Shilin He, Pinjia He, Jinyang Liu, Michael R. Lyu. [Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics](https://arxiv.org/abs/2008.06448). IEEE International Symposium on Software Reliability Engineering (ISSRE), 2023.
+ **Loghub-2.0**: Zhihan Jiang, Jinyang Liu, Junjie Huang, Yichen Li, Yintong Huo, Jiazhen Gu, Zhuangbin Chen, Jieming Zhu, Michael R. Lyu. [A Large-scale Evaluation for Log Parsing Techniques: How Far are We?](https://arxiv.org/abs/2308.10828). ACM SIGSOFT International Symposium on Software Testing and Analysis (ISSTA), 2024.

### 🌈 License
The datasets are freely available for research or academic work. For any usage or distribution of the datasets, please refer to the loghub repository URL https://github.com/logpai/loghub and cite [the loghub paper](https://github.com/logpai/loghub/blob/master/CITATION) where applicable.

### 🙋 Discussion
Welcome to [open a discussion here](https://github.com/logpai/loghub/discussions/new/choose) for any question and discussion.
