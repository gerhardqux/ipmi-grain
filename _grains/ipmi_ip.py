#!/usr/bin/env python

"""Let physical servers figure out their ipmi ip, and provide it in a grain."""

import os
import re
import subprocess


def ipmi_ip():
    """Return the IPMI IP grain."""
    if not os.path.isfile('/usr/bin/ipmitool'):
        return {}

    try:
        lan_print = subprocess.check_output(['/usr/bin/ipmitool',
                                             'lan',
                                             'print'])
    except:
        pass
    else:
        res = {}
        match = re.search(r'^IP Address\s+:\s*(.+)$',
                          lan_print,
                          re.MULTILINE)
        if match:
            res.update({
                'ipmi_ip': match.group(1)
            })

        match = re.search(r'^MAC Address\s+:\s*(.+)$',
                          lan_print,
                          re.MULTILINE)
        if match:
            res.update({
                'ipmi_mac': match.group(1)
            })

        return res

    return {}


if __name__ == '__main__':
    print(ipmi_ip())
