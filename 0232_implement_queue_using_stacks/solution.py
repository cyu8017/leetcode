# LeetCode 0232 - Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue:
    def __init__(self):
        self.input_stack: list[int] = []
        self.output_stack: list[int] = []

    def _move(self) -> None:
        if not self.output_stack:
            while self.input_stack:
                self.output_stack.append(self.input_stack.pop())

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        self._move()
        return self.output_stack.pop()

    def peek(self) -> int:
        self._move()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not self.input_stack and not self.output_stack
