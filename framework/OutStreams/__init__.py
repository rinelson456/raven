# Copyright 2017 Battelle Energy Alliance, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
  The OutStreamManagers module includes the different type of ways to output
  data available in RAVEN

  Created on April 5, 2016
  @author: maljdp
  supercedes OutStreamManager.py from alfoa (11/14/2013)
"""

from __future__ import absolute_import

## These lines ensure that we do not have to do something like:
## 'from OutStreamManagers.OutStreamPlot import OutStreamPlot' outside
## of this submodule
from .OutStreamBase import OutStreamBase
from .FilePrint import FilePrint
from .GeneralPlot import GeneralPlot as Plot

from .Factory import knownTypes
from .Factory import returnInstance
from .Factory import returnClass
