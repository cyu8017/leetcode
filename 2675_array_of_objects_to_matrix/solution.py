# LeetCode 2675 - Array of Objects to Matrix
# https://leetcode.com/problems/array-of-objects-to-matrix/

from typing import Any, Dict, List


class Solution:
    def jsonToMatrix(self, arr: List[Any]) -> List[List[Any]]:
        def is_obj(x: Any) -> bool:
            return isinstance(x, dict)

        def flatten(obj: Any, prefix: str, out: Dict[str, Any]) -> None:
            if not is_obj(obj) and not isinstance(obj, list):
                out[prefix] = obj
                return
            if isinstance(obj, list):
                if not obj:
                    return
                for i, item in enumerate(obj):
                    flatten(item, prefix + "." + str(i) if prefix else str(i), out)
                return
            keys = list(obj.keys())
            if not keys:
                return
            for k in keys:
                flatten(obj[k], prefix + "." + str(k) if prefix else str(k), out)

        maps = []
        for o in arr:
            m = {}
            flatten(o, "", m)
            maps.append(m)
        key_set = set()
        for m in maps:
            key_set.update(m.keys())
        keys = sorted(key_set)
        mat = [keys]
        for m in maps:
            mat.append([m[k] if k in m else "" for k in keys])
        return mat
