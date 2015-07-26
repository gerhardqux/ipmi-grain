#!/usr/bin/env python

import os
import re
import subprocess


def ipmi_ip():
    if os.path.isfile('/usr/bin/ipmitool'):
        try:
            lan_print = subprocess.check_output(['/usr/bin/ipmitool',
                                                 'lan',
                                                 'print'])
            for line in lan_print.split('\n'):
                match = re.match(r'^IP Address\s+:\s*(.+)$', line)
                if match:
                    return {
                        'ipmi_ip': match.group(1)
                    }
        except:
            pass
    return {
        'ipmi_ip': 'Unknown'
    }

if __name__ == '__main__':
    print(ipmi_ip())
