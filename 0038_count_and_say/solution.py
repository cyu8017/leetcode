# LeetCode 0038 - Count and Say
# https://leetcode.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n: int) -> str:
        term = "1"

        for _ in range(1, n):
            next_term: list[str] = []
            index = 0
            while index < len(term):
                count = 1
                while index + count < len(term) and term[index + count] == term[index]:
                    count += 1
                next_term.append(str(count))
                next_term.append(term[index])
                index += count
            term = "".join(next_term)

        return term
