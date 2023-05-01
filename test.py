# This Python file will generate a yaml profile in
# location: /tmp/trex_files/traffic_profile.yaml
# It will also generate a new pcap file whichwill be used in
# the yaml file
# Once that is created we can use it to run trex manually.

from trex import connect, flow_get, profile_get


hostname = "TPC-D8-11-005"

c = connect(host=hostname, mode="stf")
p = profile_get()
f = flow_get('poco_udp_6')

f.flow_configure(cps=1.0)
f.add_tunnel(tunnel='gtpu', src_ip='1.0.0.1', dst_ip='1.0.0.2', teid=1,side='')
f.add_tunnel(tunnel='vlan', vlan_tag=100, side='')
f.add_tunnel(tunnel='ether_gre', src_ip='2.0.0.1', dst_ip='2.0.0.2')

p.flow_add(f)
c.traffic_send(traffic_profile=p, multiplier=1, duration=40)
c.traffic_stats()
c.interface_cleanup()