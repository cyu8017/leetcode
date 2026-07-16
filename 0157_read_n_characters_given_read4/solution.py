# LeetCode 0157 - Read N Characters Given Read4
# https://leetcode.com/problems/read-n-characters-given-read4/


class Solution:
    def read(self, file: str, n: int) -> int:
        index = 0

        def read4(buf4: list[str]) -> int:
            nonlocal index
            count = 0
            while count < 4 and index < len(file):
                buf4[count] = file[index]
                index += 1
                count += 1
            return count

        buf = [""] * n
        copied = 0
        while copied < n:
            buf4 = [""] * 4
            count = read4(buf4)
            if count == 0:
                break
            for i in range(count):
                if copied == n:
                    break
                buf[copied] = buf4[i]
                copied += 1
        return copied
