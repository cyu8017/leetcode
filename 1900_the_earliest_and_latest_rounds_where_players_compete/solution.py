# LeetCode 1900 - The Earliest and Latest Rounds Where Players Compete
# https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/

from functools import lru_cache
from itertools import product


class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        first = firstPlayer
        second = secondPlayer

        @lru_cache(maxsize=None)
        def dfs(players: tuple[int, ...]) -> tuple[int, int]:
            count = len(players)
            first_index = players.index(first)
            second_index = players.index(second)
            if first_index + second_index == count - 1:
                return (1, 1)

            choices: list[tuple[int, ...]] = []
            for index in range(count // 2):
                left = players[index]
                right = players[count - 1 - index]
                if left in (first, second):
                    choices.append((left,))
                elif right in (first, second):
                    choices.append((right,))
                else:
                    choices.append((left, right))

            if count % 2:
                choices.append((players[count // 2],))

            earliest = 10**9
            latest = 0
            for picks in product(*choices):
                winners = tuple(sorted(picks))
                early, late = dfs(winners)
                earliest = min(earliest, early + 1)
                latest = max(latest, late + 1)
            return (earliest, latest)

        return list(dfs(tuple(range(1, n + 1))))
