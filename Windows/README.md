## Windows

This log dataset was collected by aggregating a number of logs from a lab computer running Windows 7. The original logs were located at `C:\Windows\Logs\CBS`. [CBS (Component Based Servicing)](https://blogs.technet.microsoft.com/askperf/2008/04/23/understanding-component-based-servicing/) is a componentization architecture in Windows, which works at the package/update level. The CBS architecture is far more robust and secure than the installers in previous operating systems. Users benefit from a more complete and controlled installation process that allows updates, drivers and optional components to be added while simultaneously mitigating against instability issues caused by improper or partial installation. The logs have a large size (over 27GB) and span a period of 226+ days.

### Download
The raw logs are available for downloading at https://github.com/logpai/loghub.

### Citation
If you use this dataset from loghub in your research, please cite the following papers.
+ Jieming Zhu, Shilin He, Pinjia He, Jinyang Liu, Michael R. Lyu. [Loghub: A Large Collection of System Log Datasets for AI-driven Log Analytics](https://arxiv.org/abs/2008.06448). IEEE International Symposium on Software Reliability Engineering (ISSRE), 2023.
