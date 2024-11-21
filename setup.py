#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import versioneer

from setuptools import setup
from generate_python_files import get_properties

properties = get_properties(package_name='dropbot')['LIB_PROPERTIES']

setup(name=properties['package_name'],
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description=properties['short_description'],
      long_description='\n'.join([properties['short_description'],
                                  properties['long_description']]),
      author_email=properties['author_email'],
      author=properties['author'],
      url=properties['url'],
      install_requires=['base-node-rpc>=0.23'],
      # Install data listed in `MANIFEST.in`
      include_package_data=True,
      package_data={'mr_box_peripheral_board.notebooks': ["Auto_Pump.ipynb", "LED test board.ipynb",
                                                                   "Peripheral UIs.ipynb",
                                                                   "Peripheral GTK UI.ipynb",
                                                                   "Streaming plot demo.ipynb"]},
      license='BSD-3',
      packages=['mr_box_peripheral_board',
                         'mr_box_peripheral_board.bin',
                         'mr_box_peripheral_board.notebooks',
                         'mr_box_peripheral_board.ui'])