## Windows

This log dataset was collected by aggregating a number of logs from a lab computer running Windows 7. The original logs were located at `C:\Windows\Logs\CBS`. [CBS (Component Based Servicing)](https://blogs.technet.microsoft.com/askperf/2008/04/23/understanding-component-based-servicing/) is a componentization architecture in Windows, which works at the package/update level. The CBS architecture is far more robust and secure than the installers in previous operating systems. Users benefit from a more complete and controlled installation process that allows updates, drivers and optional components to be added while simultaneously mitigating against instability issues caused by improper or partial installation. The logs have a huge size (over 27GB) and span a period of 226+ days.

Note that `Windows_2k.log` is a sample log. The raw logs can be requested from Zenodo: https://doi.org/10.5281/zenodo.1144100
