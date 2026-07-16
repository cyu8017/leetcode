# LeetCode 0591 - Tag Validator
# https://leetcode.com/problems/tag-validator/


class Solution:
    def isValid(self, code: str) -> bool:
        stack: list[str] = []
        i = 0
        n = len(code)

        while i < n:
            if code.startswith("<![CDATA[", i):
                if not stack:
                    return False
                j = code.find("]]>", i + 9)
                if j < 0:
                    return False
                i = j + 3
            elif code.startswith("</", i):
                j = code.find(">", i + 2)
                if j < 0:
                    return False
                tag = code[i + 2 : j]
                if not stack or stack[-1] != tag:
                    return False
                stack.pop()
                i = j + 1
                if not stack and i < n:
                    return False
            elif code.startswith("<", i):
                j = code.find(">", i + 1)
                if j < 0:
                    return False
                tag = code[i + 1 : j]
                if not tag or len(tag) > 9 or any(ch < "A" or ch > "Z" for ch in tag):
                    return False
                stack.append(tag)
                i = j + 1
            else:
                if not stack:
                    return False
                i += 1

        return not stack
