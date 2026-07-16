# LeetCode 1152 - Analyze User Website Visit Pattern
# https://leetcode.com/problems/analyze-user-website-visit-pattern/

from collections import defaultdict


class Solution:
    def mostVisitedPattern(self, username: list[str], timestamp: list[int], website: list[str]) -> list[str]:
        visits: dict[str, list[tuple[int, str]]] = defaultdict(list)
        for user, t, site in zip(username, timestamp, website):
            visits[user].append((t, site))
        scores: dict[tuple[str, str, str], int] = defaultdict(int)
        for user in visits:
            sites = [site for _, site in sorted(visits[user])]
            patterns = set()
            for i in range(len(sites)):
                for j in range(i + 1, len(sites)):
                    for k in range(j + 1, len(sites)):
                        patterns.add((sites[i], sites[j], sites[k]))
            for pattern in patterns:
                scores[pattern] += 1
        best = min((-count, pattern) for pattern, count in scores.items())[1]
        return list(best)
