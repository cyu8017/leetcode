# LeetCode 0751 - IP to CIDR
# https://leetcode.com/problems/ip-to-cidr/

from typing import List


class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        def ip_to_int(value: str) -> int:
            result = 0
            for part in value.split("."):
                result = result * 256 + int(part)
            return result

        def int_to_ip(value: int) -> str:
            return ".".join(str((value >> shift) & 255) for shift in (24, 16, 8, 0))

        start = ip_to_int(ip)
        answer: list[str] = []
        while n > 0:
            lowbit = start & -start if start else 1 << 32
            while lowbit > n:
                lowbit >>= 1
            mask = 32 - (lowbit.bit_length() - 1)
            answer.append(f"{int_to_ip(start)}/{mask}")
            start += lowbit
            n -= lowbit
        return answer
