# LeetCode 2722 - Join Two Arrays by ID
# https://leetcode.com/problems/join-two-arrays-by-id/

from typing import Any, Dict, List


class Solution:
    def join(self, arr1: List[Dict[str, Any]], arr2: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        by_id = {}
        for obj in arr1:
            by_id[obj["id"]] = dict(obj)
        for obj in arr2:
            if obj["id"] in by_id:
                by_id[obj["id"]].update(obj)
            else:
                by_id[obj["id"]] = dict(obj)
        return sorted(by_id.values(), key=lambda o: o["id"])
