// LeetCode 0232 - Implement Queue using Stacks
// https://leetcode.com/problems/implement-queue-using-stacks/

import java.util.ArrayDeque;
import java.util.Deque;

class MyQueue {
    private final Deque<Integer> inputStack = new ArrayDeque<>();
    private final Deque<Integer> outputStack = new ArrayDeque<>();

    private void move() {
        if (outputStack.isEmpty()) {
            while (!inputStack.isEmpty()) {
                outputStack.push(inputStack.pop());
            }
        }
    }

    public void push(int x) {
        inputStack.push(x);
    }

    public int pop() {
        move();
        return outputStack.pop();
    }

    public int peek() {
        move();
        return outputStack.peek();
    }

    public boolean empty() {
        return inputStack.isEmpty() && outputStack.isEmpty();
    }
}
