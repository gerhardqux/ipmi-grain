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
                                 {'ipmi_ip': 'Unknown'})

    def test_ipmi_localhost(self):
        with mock.patch('os.path.isfile') as isfile, \
             mock.patch('subprocess.check_output') as chk_out:

            fake_isfile = True
            isfile.return_value = fake_isfile

            fake_chk_out = str('IP Address : 127.0.0.1')
            chk_out.return_value = fake_chk_out

            self.assertDictEqual(ipmi_ip.ipmi_ip(),
                                 {'ipmi_ip': '127.0.0.1'})

    def test_ipmi_empty(self):
        with mock.patch('os.path.isfile') as isfile, \
             mock.patch('subprocess.check_output') as chk_out:

            fake_isfile = True
            isfile.return_value = fake_isfile

            fake_chk_out = str('')
            chk_out.return_value = fake_chk_out

            self.assertDictEqual(ipmi_ip.ipmi_ip(),
                                 {'ipmi_ip': 'Unknown'})


if __name__ == '__main__':
    unittest.main()
