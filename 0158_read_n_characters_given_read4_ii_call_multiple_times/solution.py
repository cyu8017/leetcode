# LeetCode 0158 - Read N Characters Given read4 II - Call Multiple Times
# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

from typing import List


class Solution:
    def read(self, file: str, queries: List[int]) -> List[int]:
        file_index = 0
        buffer = [""] * 4
        buffer_size = 0
        buffer_index = 0

        def read4(buf4: list[str]) -> int:
            nonlocal file_index
            count = 0
            while count < 4 and file_index < len(file):
                buf4[count] = file[file_index]
                file_index += 1
                count += 1
            return count

        def read_once(n: int) -> int:
            nonlocal buffer_size, buffer_index
            copied = 0
            while copied < n:
                if buffer_index == buffer_size:
                    buffer_size = read4(buffer)
                    buffer_index = 0
                    if buffer_size == 0:
                        break
                while copied < n and buffer_index < buffer_size:
                    copied += 1
                    buffer_index += 1
            return copied

        return [read_once(query) for query in queries]
