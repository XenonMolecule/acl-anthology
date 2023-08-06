# Copyright 2023 Marcel Bollmann <marcel@bollmann.me>
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

from acl_anthology.people import PersonIndex


def test_load_variant_list(anthology_stub):
    index = PersonIndex(anthology_stub)
    index._load_variant_list()
    for pid in (
        "pranav-a",
        "pranav-anand",
        "yang-liu-edinburgh",
        "yang-liu-icsi",
        "yang-liu-ict",
        "steven-krauwer",
    ):
        assert pid in index.people
