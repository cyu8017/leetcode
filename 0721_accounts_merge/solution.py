# LeetCode 0721 - Accounts Merge
# https://leetcode.com/problems/accounts-merge/

from collections import defaultdict
from typing import List


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent: dict[str, str] = {}
        email_name: dict[str, str] = {}

        def find(x: str) -> str:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a: str, b: str) -> None:
            parent[find(a)] = find(b)

        for account in accounts:
            name = account[0]
            first = account[1]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                email_name[email] = name
                union(first, email)

        groups: dict[str, list[str]] = defaultdict(list)
        for email in parent:
            groups[find(email)].append(email)

        result: list[list[str]] = []
        for emails in groups.values():
            result.append([email_name[emails[0]]] + sorted(emails))
        return result
