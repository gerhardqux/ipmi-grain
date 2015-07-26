#!/usr/bin/env python

"""Let physical servers figure out their ipmi ip, and provide it in a grain."""

import os
import re
import subprocess


def ipmi_ip():
    """Return the IPMI IP grain."""
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
