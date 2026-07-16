// LeetCode 0232 - Implement Queue using Stacks
// https://leetcode.com/problems/implement-queue-using-stacks/

#include <stack>

using namespace std;

class MyQueue {
    stack<int> inputStack;
    stack<int> outputStack;

    void move() {
        if (outputStack.empty()) {
            while (!inputStack.empty()) {
                outputStack.push(inputStack.top());
                inputStack.pop();
            }
        }
    }

public:
    MyQueue() {}

    void push(int x) {
        inputStack.push(x);
    }

    int pop() {
        move();
        int value = outputStack.top();
        outputStack.pop();
        return value;
    }

    int peek() {
        move();
        return outputStack.top();
    }

    bool empty() {
        return inputStack.empty() && outputStack.empty();
    }
};
