# coding: utf-8
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = 'Jeremy Emerson'

import feconf
import oppia.storage.state.models as state_models

from django.utils import unittest


class StateModelUnitTests(unittest.TestCase):
    """Test the state model."""

    def setUp(self):
        """Loads the default widgets and creates a sample exploration."""
        super(StateModelUnitTests, self).setUp()

    def test_state_class(self):
        """Test State Class."""
        state = state_models.State(id='The exploration hash id')

        # A new state should have a default name property.
        self.assertEqual(state.name, feconf.DEFAULT_STATE_NAME)

        state.put()