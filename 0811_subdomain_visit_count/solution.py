# LeetCode 0811 - Subdomain Visit Count
# https://leetcode.com/problems/subdomain-visit-count/

from collections import Counter
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts: Counter[str] = Counter()
        for item in cpdomains:
            count_str, domain = item.split()
            count = int(count_str)
            parts = domain.split(".")
            for i in range(len(parts)):
                counts[".".join(parts[i:])] += count
        return [f"{count} {domain}" for domain, count in counts.items()]
