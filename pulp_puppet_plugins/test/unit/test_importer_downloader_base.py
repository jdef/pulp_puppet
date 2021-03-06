# -*- coding: utf-8 -*-
#
# Copyright © 2012 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public
# License as published by the Free Software Foundation; either version
# 2 of the License (GPLv2) or (at your option) any later version.
# There is NO WARRANTY for this software, express or implied,
# including the implied warranties of MERCHANTABILITY,
# NON-INFRINGEMENT, or FITNESS FOR A PARTICULAR PURPOSE. You should
# have received a copy of GPLv2 along with this software; if not, see
# http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

import unittest

from pulp_puppet.plugins.importers.downloaders import base

class BaseDownloaderTests(unittest.TestCase):

    def test_not_implemented(self):
        # Ensures the base class properly raises NotImplementedError for
        # appropriate APIs

        b = base.BaseDownloader(None, None, None, None)
        self.assertRaises(NotImplementedError, b.retrieve_metadata, None)
        self.assertRaises(NotImplementedError, b.retrieve_module, None, None)
        self.assertRaises(NotImplementedError, b.cleanup_module, None)
