# Trex
# Trex...
### AMENI

# SETUP GUIDE :

## 1. Setup NIC ports DPDK drivers

1/ Move to Trex directory 

```bash
cd /opt/trex/v2.XX/
```
2/ Identify the ports:

```bash
./dpdk_setup_ports.py -s
```

```bash
modprobe uio
insmod ko/src/igb_uio.ko
./dpdk_nic_bind.py -b igb_uio #add 2 port Ids
```
