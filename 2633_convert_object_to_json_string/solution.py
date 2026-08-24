# LeetCode 2633 - Convert Object to JSON String
# https://leetcode.com/problems/convert-object-to-json-string/

from typing import Any


class Solution:
    def jsonStringify(self, object: Any) -> str:
        if object is None:
            return "null"
        t = type(object)
        if t is str:
            return '"' + object + '"'
        if t is bool:
            return "true" if object else "false"
        if t is int or t is float:
            return str(object)
        if isinstance(object, list):
            return "[" + ",".join(self.jsonStringify(x) for x in object) + "]"
        keys = list(object.keys())
        return "{" + ",".join('"' + str(k) + '":' + self.jsonStringify(object[k]) for k in keys) + "}"
