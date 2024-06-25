from scapy.all import sniff, wrpcap
import logging

def capture_packets(interface, count):
    logging.info(f"بدء التقاط الحزم على الواجهة {interface}")
    packets = sniff(iface=interface, count=count)
    wrpcap('captures/packets.pcap', packets)
    return 'captures/packets.pcap'
