// LeetCode 0716 - Max Stack
// https://leetcode.com/problems/max-stack/

import java.util.*;

class MaxStack {
    private final List<Integer> stack = new ArrayList<>();
    private final List<Integer> maxes = new ArrayList<>();

    public MaxStack() {}

    public void push(int x) {
        stack.add(x);
        maxes.add(maxes.isEmpty() ? x : Math.max(x, maxes.get(maxes.size() - 1)));
    }

    public int pop() {
        maxes.remove(maxes.size() - 1);
        return stack.remove(stack.size() - 1);
    }

    public int top() { return stack.get(stack.size() - 1); }

    public int peekMax() { return maxes.get(maxes.size() - 1); }

    public int popMax() {
        int maxVal = peekMax();
        List<Integer> buffer = new ArrayList<>();
        while (top() != maxVal) buffer.add(pop());
        pop();
        for (int i = buffer.size() - 1; i >= 0; i--) push(buffer.get(i));
        return maxVal;
    }
}
