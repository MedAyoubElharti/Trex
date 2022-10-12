# SETUP GUIDE :


## 1. Install Cisco TRex

1/ Create Trex directory 

```bash
mkdir -p /opt/trex
```

2/ Move to Trex directory 

```bash
cd /opt/trex/v2.XX/
```
3/ Download the lqst version of Trex

```bash
wget --no-cache --no-check-certificate https://trex-tgn.cisco.com/trex/release/latest
```
4/ Untar the tar file

```bash
tar -xzvf latest
```
## 2. Setup NIC ports DPDK drivers

1/ Move to Trex directory 

```bash
cd /opt/trex/v2.XX/
```
2/ Identify the ports:

```bash
./dpdk_setup_ports.py -s
```
3/ Insert the kernel driver and bind NIC ports
```bash
modprobe uio
insmod ko/src/igb_uio.ko
./dpdk_nic_bind.py -b igb_uio #add 2 port Ids
```
