# LeetCode 0353 - Design Snake Game
# https://leetcode.com/problems/design-snake-game/

from collections import deque
from typing import List


class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.score = 0
        self.snake: deque[tuple[int, int]] = deque([(0, 0)])
        self.body = {(0, 0)}

    def move(self, direction: str) -> int:
        row, col = self.snake[0]
        if direction == "U":
            row -= 1
        elif direction == "D":
            row += 1
        elif direction == "L":
            col -= 1
        else:
            col += 1

        new_head = (row, col)
        if row < 0 or row >= self.height or col < 0 or col >= self.width:
            return -1

        will_eat = (
            self.food_index < len(self.food)
            and [row, col] == self.food[self.food_index]
        )

        if not will_eat:
            tail = self.snake.pop()
            self.body.remove(tail)

        if new_head in self.body:
            return -1

        self.snake.appendleft(new_head)
        self.body.add(new_head)

        if will_eat:
            self.score += 1
            self.food_index += 1

        return self.score
