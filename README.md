<p align="center"> <a href="https://github.com/logpai"> <img src="https://cdn.jsdelivr.net/gh/logpai/logpai.github.io@master/img/logpai_logo.jpg" width="480"></a></p>


# Loghub

<div>
<a href="https://github.com/logpai/loghub/stargazers"><img src="http://bytecrank.com/nastyox/reporoster/php/stargazersSVG.php?user=logpai&repo=loghub" width="600"/><a/>
</div>

Loghub maintains a collection of system logs, which are freely accessible for AI-driven log analytics research. Some of the logs are production data released from previous studies, while some others are collected from real systems in our lab environment. Wherever possible, the logs are NOT sanitized, anonymized or modified in any way. These log datasets are freely available for research or academic work.

🤗 We proudly announce that the loghub datasets have attained total <a href="https://doi.org/10.5281/zenodo.1144100"><img src="https://img.shields.io/endpoint?&url=https://cdn.jsdelivr.net/gh/logpai/loghub@zenodo/downloads.json&labelColor=1AE&color=DDEEFF&style=flat&label=Downloads"></a> by more than [**450 organizations**](https://github.com/logpai/loghub/wiki/Loghub-download-list) from both industry and academia.

### Logs currently available

🔗 Get raw logs via hyperlinks in the Download column.

| Dataset              | Description | Labeled | Time Span  |  #Lines  |   Raw Size   |  Download  |
| :---------------------------- | :--------|  :--------: | --------: | ---------: | ------: | :------: | 
|<tr><th colspan=7 align="center">:open_file_folder: **Distributed systems**</th></tr>|
| [HDFS_v1](./HDFS#hdfs_v1)     | Hadoop distributed file system log | :heavy_check_mark: | 38.7 hours | 11,175,629  |  1.47GB  | [:link:](https://zenodo.org/records/8196385/files/HDFS_v1.zip?download=1)   |      
| [HDFS_v2](./HDFS#hdfs_v2)     | Hadoop distributed file system log|  |    N.A.    | 71,118,073  | 16.06GB  | [:link:](https://zenodo.org/records/8196385/files/HDFS_v2.zip?download=1)  |
| [HDFS_v3](./HDFS#hdfs_v3_tracebench)     | Instrumented HDFS trace log (TraceBench) | :heavy_check_mark: |    N.A.    | 14,778,079  | 2.96GB  | [:link:](https://zenodo.org/records/8196385/files/HDFS_v3_TraceBench.zip?download=1)  |
| [Hadoop](./Hadoop)            |  Hadoop mapreduce job log | :heavy_check_mark: |   N.A.    |   394,308   | 48.61MB  |  [:link:](https://zenodo.org/records/8196385/files/Hadoop.zip?download=1)  |
| [Spark](./Spark)              | Spark job log ||    N.A.    | 33,236,604  |  2.75GB  | [:link:](https://zenodo.org/records/8196385/files/Spark.tar.gz?download=1)  |                            
| [Zookeeper](./Zookeeper)      | ZooKeeper service log | | 26.7 days  |   74,380    | 9.95MB  |  [:link:](https://zenodo.org/records/8196385/files/Zookeeper.tar.gz?download=1)   | 
| [OpenStack](./OpenStack)      |  OpenStack infrastructure log | :heavy_check_mark: |  N.A.    |   207,820   | 58.61MB  |  [:link:](https://zenodo.org/records/8196385/files/OpenStack.tar.gz?download=1)  |    
|<tr><th colspan=7 align="center">:open_file_folder: **Super computers**</th></tr>|
| [BGL](./BGL)          | Blue Gene/L supercomputer log | :heavy_check_mark: | 214.7 days |  4,747,963  | 708.76MB |  [:link:](https://zenodo.org/records/8196385/files/BGL.zip?download=1)   |
| [HPC](./HPC)                  |  High performance cluster log | |  N.A.    |   433,489   | 32.00MB  |  [:link:](https://zenodo.org/records/8196385/files/HPC.zip?download=1)  |           
| [Thunderbird](./Thunderbird)  |  Thunderbird supercomputer log | :heavy_check_mark: | 244 days  | 211,212,192 | 29.60GB  | [:link:](https://zenodo.org/records/8196385/files/Thunderbird.tar.gz?download=1)  |
|<tr><th colspan=7 align="center">:open_file_folder: **Operating systems**</th></tr>|  
| [Windows](./Windows)          | Windows event log | | 226.7 days | 114,608,388 | 26.09GB  | [:link:](https://zenodo.org/records/8196385/files/Windows.tar.gz?download=1)   |    
| [Linux](./Linux)              | Linux system log | | 263.9 days |   25,567    |  2.25MB  |  [:link:](https://zenodo.org/records/8196385/files/Linux.tar.gz?download=1)  |
| [Mac](./Mac)                  | Mac OS log | | 7.0 days  |   117,283   | 16.09MB  | [:link:](https://zenodo.org/records/8196385/files/Mac.tar.gz?download=1)  |
|<tr><th colspan=7 align="center">:open_file_folder: **Mobile systems**</th></tr>|  
| [Android_v1](./Android#android_v1)          |  Android framework log | |  N.A.    | 1,555,005  |  183.37MB | [:link:](https://zenodo.org/records/8196385/files/Android_v1.zip?download=1) |
| [Android_v2](./Android#android_v2)          |  Android framework log | |  N.A.    | 30,348,042  | 3.38GB  | [:link:](https://zenodo.org/records/8196385/files/Android_v2.zip?download=1)  |
| [HealthApp](./HealthApp)      | Health app log  | | 10.5 days  |   253,395   | 22.44MB  | [:link:](https://zenodo.org/records/8196385/files/HealthApp.tar.gz?download=1)  |
|<tr><th colspan=7 align="center">:open_file_folder: **Server applications**</th></tr>|            
| [Apache](./Apache) | Apache web server error log | | 263.9 days |   56,481    |  4.90MB  | [:link:](https://zenodo.org/records/8196385/files/Apache.tar.gz?download=1)   |                     
| [OpenSSH](./OpenSSH)          | OpenSSH server log | | 28.4 days  |   655,146   | 70.02MB  | [:link:](https://zenodo.org/records/8196385/files/SSH.tar.gz?download=1) |
|<tr><th colspan=7 align="center">:open_file_folder: **Standalone software**</th></tr>|                           
| [Proxifier](./Proxifier)      |   Proxifier software log | | N.A.    |   21,329    |  2.42MB  |   [:link:](https://zenodo.org/records/8196385/files/Proxifier.tar.gz?download=1) |                                           


### 🔥 Citation

Please cite the following paper if you use the loghub datasets in your research.

+ Jieming Zhu, Shilin He, Pinjia He, Jinyang Liu, Michael R. Lyu. [Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics](https://arxiv.org/abs/2008.06448). IEEE International Symposium on Software Reliability Engineering (ISSRE), 2023.


### Publications using loghub datasets

| Publication       | Paper Title | 
| :----: | :---- | 
| DSN'07 | Adam J. Oliner, Jon Stearley. [What Supercomputers Say: A Study of Five System Logs](http://ieeexplore.ieee.org/document/4273008/). IEEE/IFIP International Conference on Dependable Systems and Networks (DSN), 2007. |
| SOSP'09  |  Wei Xu, Ling Huang, Armando Fox, David A. Patterson, Michael I. Jordan. [Detecting Large-Scale System Problems by Mining Console Logs](https://www.sigops.org/sosp/sosp09/papers/xu-sosp09.pdf). ACM Symposium on Operating Systems Principles (SOSP), 2009. |
| KDD'09 | Adetokunbo Makanju, A. Nur Zincir-Heywood, Evangelos E. Milios. [Clustering Event Logs Using Iterative Partitioning](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.503.7668&rep=rep1&type=pdf). ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD), 2009. |
| ISSRE'16 | Shilin He, Jieming Zhu, Pinjia He, Michael R. Lyu. [Experience Report: System Log Analysis for Anomaly Detection](https://jiemingzhu.github.io/pub/slhe_issre2016.pdf). IEEE International Symposium on Software Reliability Engineering (ISSRE), 2016. |
| DSN'16 | Pinjia He, Jieming Zhu, Shilin He, Jian Li, Michael R. Lyu. [An Evaluation Study on Log Parsing and Its Use in Log Mining](https://jiemingzhu.github.io/pub/pjhe_dsn2016.pdf). IEEE/IFIP International Conference on Dependable Systems and Networks (DSN), 2016. |
| ICSE'16 | Qingwei Lin, Hongyu Zhang, Jian-Guang Lou, Yu Zhang, Xuewei Chen. [Log Clustering Based Problem Identification for Online Service Systems](http://ieeexplore.ieee.org/document/7883294/). International Conference on Software Engineering (ICSE), 2016. |
| ICWS'17 | Pinjia He, Jieming Zhu, Zibin Zheng, Michael R. Lyu. [Drain: An Online Log Parsing Approach with Fixed Depth Tree](https://jiemingzhu.github.io/pub/pjhe_icws2017.pdf). IEEE International Conference on Web Services (ICWS), 2017. |
| CCS'17 | Min Du, Feifei Li, Guineng Zheng, Vivek Srikumar. [DeepLog: Anomaly Detection and Diagnosis from System Logs through Deep Learning](https://acmccs.github.io/papers/p1285-duA.pdf). ACM Conference on Computer and Communications Security (CCS), 2017. |
| TDSC'18 | Pinjia He, Jieming Zhu, Shilin He, Jian Li, Michael R. Lyu. [Towards Automated Log Parsing for Large-Scale Log Data Analysis](https://ieeexplore.ieee.org/document/8067504). IEEE Transactions on Dependable and Secure Computing (TDSC), 2018. |
| TKDE'18 | Min Du, Feifei Li. [Spell: Online Streaming Parsing of Large Unstructured System Logs](https://ieeexplore.ieee.org/abstract/document/8489912). IEEE Transactions on Knowledge and Data Engineering (TKDE), 2018. |
| ASE'19 |  Jinyang Liu, Jieming Zhu, Shilin He, Pinjia He, Zibin Zheng, Michael R. Lyu. [Logzip: Extracting Hidden Structures via Iterative Clustering for Log Compression](https://arxiv.org/abs/1910.00409). IEEE/ACM International Conference on Automated Software Engineering (ASE), 2019. |
| ICSE'19 | Jieming Zhu, Shilin He, Jinyang Liu, Pinjia He, Qi Xie, Zibin Zheng, Michael R. Lyu. [Tools and Benchmarks for Automated Log Parsing](https://arxiv.org/pdf/1811.03509.pdf). International Conference on Software Engineering (ICSE), 2019. |
| ICSE'22 | Zanis Ali Khan, Donghwan Shin, Domenico Bianculli, Lionel Briand. [Guidelines for Assessing the Accuracy of Log Message Template Identification Techniques](https://dl.acm.org/doi/pdf/10.1145/3510003.3510101). International Conference on Software Engineering (ICSE), 2023. |
| ICSE'23 | Van-Hoang Le, Hongyu Zhang. [Log Parsing with Prompt-based Few-shot Learning](https://arxiv.org/abs/2302.07435). International Conference on Software Engineering (ICSE), 2023. |
| ICSE'23 | Zhenhao Li, Chuan Luo, Tse-Hsun Chen, Weiyi Shang, Shilin He, Qingwei Lin, Dongmei Zhang. [Did We Miss Something Important? Studying and Exploring Variable-Aware Log Abstraction](https://arxiv.org/abs/2304.11391). International Conference on Software Engineering (ICSE), 2023. |
| ICSE'23 | Yintong Huo, Yuxin Su, Cheryl Lee, Michael R. Lyu. [SemParser: A Semantic Parser for Log Analysis](https://arxiv.org/abs/2112.12636). International Conference on Software Engineering (ICSE), 2023. |
| WWW'23 | Liming Wang, Hong Xie, Ye Li, Jian Tan, John C.S. Lui. [Interactive Log Parsing via Light-weight User Feedback](https://arxiv.org/abs/2301.12225). ACM Web Conference, 2023. | 
| TSC'23 | Siyu Yu, Pinjia He, Ningjiang Chen, Yifan Wu. [Brain: Log Parsing with Bidirectional Parallel Tree](https://ieeexplore.ieee.org/document/10109145). IEEE Transaction on Severice Computing, 2023. |

:bulb: If you use loghub datasets in your paper, please feel free to make a PR to add your paper to the table.

### Discussion
Welcome to join our WeChat group for any question and discussion. Alternatively, you can [open a discussion here](https://github.com/logpai/loghub/discussions/new/choose).

![Scan QR code](https://cdn.jsdelivr.net/gh/logpai/logpai.github.io@master/img/wechat.png)

### 🌈 License
The datasets are freely available for research or academic work. For any usage or distribution of the datasets, please refer to the loghub repository URL https://github.com/logpai/loghub and cite [the loghub paper](https://github.com/logpai/loghub/blob/master/CITATION) where applicable.
