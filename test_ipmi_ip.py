#!/usr/bin/python

import unittest
import mock

import ipmi_ip


class IPMIIPTest(unittest.TestCase):
    def test_ipmi_unknown(self):
        with mock.patch('os.path.isfile') as isfile:
            fake_isfile = False
            isfile.return_value = fake_isfile
            self.assertDictEqual(ipmi_ip.ipmi_ip(),
                                 {})

    def test_ipmi_localhost(self):
        with mock.patch('os.path.isfile') as isfile, \
             mock.patch('subprocess.check_output') as chk_out:

            fake_isfile = True
            isfile.return_value = fake_isfile

            fake_chk_out = str('IP Address : 127.0.0.1')
            chk_out.return_value = fake_chk_out

            self.assertDictEqual(ipmi_ip.ipmi_ip(),
                                 {'ipmi_ip': '127.0.0.1'})

    def test_ipmi_multiline(self):
        with mock.patch('os.path.isfile') as isfile, \
             mock.patch('subprocess.check_output') as chk_out:

            fake_isfile = True
            isfile.return_value = fake_isfile

            fake_chk_out = str(
                "Set in Progress         : Set Complete\n"
                "Auth Type Support       : \n"
                "Auth Type Enable        : Callback : \n"
                "                        : User     : \n"
                "                        : Operator : \n"
                "                        : Admin    : MD2 PASSWORD OEM \n"
                "                        : OEM      : NONE MD2 PASSWORD \n"
                "IP Address Source       : Static Address\n"
                "IP Address              : 192.168.42.42\n"
                "Subnet Mask             : 255.255.255.0\n"
                "MAC Address             : 52:54:00:49:5c:13\n"
                "BMC ARP Control         : ARP Responses Enabled, Gratuitous ARP Disabled\n"
                "Gratituous ARP Intrvl   : 0.0 seconds\n"
                "Default Gateway IP      : 0.0.0.0\n"
                "802.1q VLAN ID          : Disabled\n"
                "802.1q VLAN Priority    : 0\n"
                "Cipher Suite Priv Max   : Not Available\n")

            chk_out.return_value = fake_chk_out

            self.assertDictEqual(ipmi_ip.ipmi_ip(),
                                 {'ipmi_ip': '192.168.42.42'})

    def test_ipmi_empty(self):
        with mock.patch('os.path.isfile') as isfile, \
             mock.patch('subprocess.check_output') as chk_out:

            fake_isfile = True
            isfile.return_value = fake_isfile

            fake_chk_out = str('')
            chk_out.return_value = fake_chk_out

            self.assertDictEqual(ipmi_ip.ipmi_ip(),
                                 {})


if __name__ == '__main__':
    unittest.main()
