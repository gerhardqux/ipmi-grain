from distutils.core import setup
setup(name='ipmi_ip',
      description='Provide the IPMI IP of a server in a salt grain',
      author='Gerhard Muntingh',
      version='0.1',
      package_dir={'': '_grains'},
      py_modules=['ipmi_ip'],
      )
