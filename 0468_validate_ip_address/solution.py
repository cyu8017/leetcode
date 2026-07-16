# LeetCode 0468 - Validate IP Address
# https://leetcode.com/problems/validate-ip-address/


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if self._is_ipv4(queryIP):
            return "IPv4"
        if self._is_ipv6(queryIP):
            return "IPv6"
        return "Neither"

    def _is_ipv4(self, address: str) -> bool:
        parts = address.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit() or len(part) > 1 and part[0] == "0":
                return False
            if len(part) == 0 or len(part) > 3:
                return False
            value = int(part)
            if value > 255:
                return False
        return True

    def _is_ipv6(self, address: str) -> bool:
        parts = address.split(":")
        if len(parts) != 8:
            return False
        hex_digits = set("0123456789abcdefABCDEF")
        for part in parts:
            if not part or len(part) > 4:
                return False
            if any(char not in hex_digits for char in part):
                return False
        return True
