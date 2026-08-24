# LeetCode 3860 - Unique Email Groups
# https://leetcode.com/problems/unique-email-groups/

from typing import List, Set


class Solution:
    def uniqueEmailGroups(self, emails: List[str]) -> int:
        st: Set[str] = set()
        for email in emails:
            at = email.find("@")
            local = email[:at]
            domain = email[at + 1 :].lower()
            plus = local.find("+")
            if plus >= 0:
                local = local[:plus]
            cleaned = ""
            for c in local:
                if c != ".":
                    cleaned += c.lower()
            st.add(cleaned + domain)
        return len(st)
