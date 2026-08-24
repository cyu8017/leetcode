# LeetCode 2759 - Convert JSON String to Object
# https://leetcode.com/problems/convert-json-string-to-object/

from typing import Any


class Solution:
    def jsonParse(self, s: str) -> Any:
        i = 0

        def parse() -> Any:
            nonlocal i
            if s[i] == '"':
                i += 1
                out = []
                while s[i] != '"':
                    out.append(s[i])
                    i += 1
                i += 1
                return "".join(out)
            if s[i] == "t":
                i += 4
                return True
            if s[i] == "f":
                i += 5
                return False
            if s[i] == "n":
                i += 4
                return None
            if s[i] == "[":
                i += 1
                arr = []
                if s[i] == "]":
                    i += 1
                    return arr
                while True:
                    arr.append(parse())
                    if s[i] == ",":
                        i += 1
                        continue
                    i += 1
                    return arr
            if s[i] == "{":
                i += 1
                obj = {}
                if s[i] == "}":
                    i += 1
                    return obj
                while True:
                    key = parse()
                    i += 1
                    obj[key] = parse()
                    if s[i] == ",":
                        i += 1
                        continue
                    i += 1
                    return obj
            start = i
            if s[i] == "-":
                i += 1
            while i < len(s) and (s[i].isdigit() or s[i] == "."):
                i += 1
            num = s[start:i]
            return float(num) if "." in num else int(num)

        return parse()
