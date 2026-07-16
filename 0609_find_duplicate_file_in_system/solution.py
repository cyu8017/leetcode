# LeetCode 0609 - Find Duplicate File in System
# https://leetcode.com/problems/find-duplicate-file-in-system/

from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths: dict[str, list[str]] = defaultdict(list)

        for entry in paths:
            parts = entry.split(" ")
            directory = parts[0]
            for file_info in parts[1:]:
                name, _, rest = file_info.partition("(")
                content = rest[:-1]
                content_to_paths[content].append(f"{directory}/{name}")

        return [group for group in content_to_paths.values() if len(group) > 1]
