# LeetCode 0913 - Cat and Mouse
# https://leetcode.com/problems/cat-and-mouse/

from collections import deque


class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        n = len(graph)
        DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2
        states = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]
        out_degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]
        queue: deque[tuple[int, int, int, int]] = deque()

        for cat in range(n):
            for mouse in range(n):
                out_degree[cat][mouse][0] = len(graph[mouse])
                out_degree[cat][mouse][1] = len(graph[cat]) - graph[cat].count(0)

        for cat in range(1, n):
            for move in range(2):
                states[cat][0][move] = MOUSE_WIN
                queue.append((cat, 0, move, MOUSE_WIN))
                states[cat][cat][move] = CAT_WIN
                queue.append((cat, cat, move, CAT_WIN))

        while queue:
            cat, mouse, move, state = queue.popleft()
            if cat == 2 and mouse == 1 and move == 0:
                return state
            prev_move = move ^ 1
            for prev in graph[cat if prev_move else mouse]:
                prev_cat = prev if prev_move else cat
                if prev_cat == 0:
                    continue
                prev_mouse = mouse if prev_move else prev
                if states[prev_cat][prev_mouse][prev_move]:
                    continue
                if (
                    (prev_move == 0 and state == MOUSE_WIN)
                    or (prev_move == 1 and state == CAT_WIN)
                    or out_degree[prev_cat][prev_mouse][prev_move] == 1
                ):
                    states[prev_cat][prev_mouse][prev_move] = state
                    queue.append((prev_cat, prev_mouse, prev_move, state))
                else:
                    out_degree[prev_cat][prev_mouse][prev_move] -= 1

        return states[2][1][0]
