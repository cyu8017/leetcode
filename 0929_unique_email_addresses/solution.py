# LeetCode 0929 - Unique Email Addresses
# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        normalized = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            normalized.add(local + "@" + domain)
        return len(normalized)
