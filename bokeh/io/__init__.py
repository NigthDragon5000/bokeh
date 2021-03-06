#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2019, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------
'''

'''

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals

import logging
log = logging.getLogger(__name__)

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports

# External Imports

# Bokeh imports

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

__all__ = (
    'curdoc',
    'export_png',
    'export_svgs',
    'install_notebook_hook',
    'push_notebook',
    'output_file',
    'output_notebook',
    'save',
    'show',
)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

from .doc import curdoc

from .export import export_png
from .export import export_svgs

from .notebook import install_notebook_hook
from .notebook import push_notebook

from .output import output_file
from .output import output_notebook
from .output import reset_output

from .saving import save

from .showing import show

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------

from .notebook import install_jupyter_hooks
install_jupyter_hooks()
del install_jupyter_hooks
