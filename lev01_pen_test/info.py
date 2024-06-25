import nmap
import logging

def gather_info(target):
    logging.info(f"جمع المعلومات على {target}")
    nm = nmap.PortScanner()
    nm.scan(target, arguments='-O')
    os_info = nm[target]['osclass'][0]['osfamily'] if 'osclass' in nm[target] else 'Unknown'
    return os_info
