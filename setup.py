#!/usr/bin/env python3.7

# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='Calima',
      version='2.0.0',
      description='Python interface for Pax Calima Fan (Bleak)',
      long_description=readme(),
      keywords='pax calima fan bluetooth ble',
      author='Theo Holmberg',
      author_email='theo.holmberg@p33.se',
      url='https://github.com/PotatisGrizen/pycalima',
      license='Apache 2.0',
      packages=['pycalima'],
      install_requires=['bleak'],
      entry_points ={
        'console_scripts': ['calima=pycalima.cmdline:main'],
      },
      include_package_data=True)
