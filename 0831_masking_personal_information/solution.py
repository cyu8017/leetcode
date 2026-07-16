# LeetCode 0831 - Masking Personal Information
# https://leetcode.com/problems/masking-personal-information/

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            name, domain = s.lower().split("@")
            return f"{name[0]}*****{name[-1]}@{domain}"
        digits = [ch for ch in s if ch.isdigit()]
        local = "".join(digits[-4:])
        country = len(digits) - 10
        if country == 0:
            return f"***-***-{local}"
        return "+" + "*" * country + f"-***-***-{local}"
