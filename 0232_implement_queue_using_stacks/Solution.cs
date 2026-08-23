// LeetCode 0232 - Implement Queue using Stacks
// https://leetcode.com/problems/implement-queue-using-stacks/

using System.Collections.Generic;

public class MyQueue {
    private readonly Stack<int> inputStack = new Stack<int>();
    private readonly Stack<int> outputStack = new Stack<int>();

    private void Move() {
        if (outputStack.Count == 0) {
            while (inputStack.Count > 0) {
                outputStack.Push(inputStack.Pop());
            }
        }
    }

    public void Push(int x) {
        inputStack.Push(x);
    }

    public int Pop() {
        Move();
        return outputStack.Pop();
    }

    public int Peek() {
        Move();
        return outputStack.Peek();
    }

    public bool Empty() {
        return inputStack.Count == 0 && outputStack.Count == 0;
    }
}
