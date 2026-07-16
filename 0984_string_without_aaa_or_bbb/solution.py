# LeetCode 0984 - String Without AAA or BBB
# https://leetcode.com/problems/string-without-aaa-or-bbb/

class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans: list[str] = []
        while a or b:
            if len(ans) >= 2 and ans[-1] == ans[-2]:
                write_a = ans[-1] == "b"
            else:
                write_a = a >= b
            if write_a:
                ans.append("a")
                a -= 1
            else:
                ans.append("b")
                b -= 1
        return "".join(ans)
