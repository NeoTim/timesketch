# Copyright 2020 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""E2E tests of Timesketch query functionality."""

from . import interface
from . import manager


class QueryTest(interface.BaseEndToEndTest):
    NAME = 'query_test'

    def __init__(self):
        super(QueryTest, self).__init__()

    def run(self):
        self.import_timeline('evtx.plaso')
        response_json = self.sketch.explore(query_string="*")
        count = response_json.get('meta', {}).get('es_total_count', 0)
        self.assertions.assertEqual(count, 3205)


manager.EndToEndTestManager.register_test(QueryTest)
