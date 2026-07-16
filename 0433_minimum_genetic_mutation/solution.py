# LeetCode 0433 - Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/

from collections import deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        if startGene == endGene:
            return 0
        valid = set(bank)
        if endGene not in valid:
            return -1

        genes = "ACGT"
        queue: deque[tuple[str, int]] = deque([(startGene, 0)])
        visited = {startGene}

        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            chars = list(gene)
            for index in range(len(chars)):
                original = chars[index]
                for letter in genes:
                    if letter == original:
                        continue
                    chars[index] = letter
                    candidate = "".join(chars)
                    if candidate in valid and candidate not in visited:
                        visited.add(candidate)
                        queue.append((candidate, steps + 1))
                chars[index] = original

        return -1
