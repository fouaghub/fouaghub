  #lev01_pen_test/core.py
import nmap
import logging

def port_scan(target):
    logging.info(f"بدء فحص المنافذ على {target}")
    nm = nmap.PortScanner()
    nm.scan(target, '1-65535')
    results = []
    for host in nm.all_hosts():
        result = {
            'host': host,
            'hostname': nm[host].hostname(),
            'state': nm[host].state(),
            'protocols': []
        }
        for proto in nm[host].all_protocols():
            proto_data = {'protocol': proto, 'ports': []}
            lport = nm[host][proto].keys()
            for port in lport:
                proto_data['ports'].append({
                    'port': port,
                    'state': nm[host][proto][port]['state']
                })
            result['protocols'].append(proto_data)
        results.append(result)
    return results
