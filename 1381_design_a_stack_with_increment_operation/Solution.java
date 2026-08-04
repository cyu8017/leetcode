// LeetCode 1381 - Design A Stack With Increment Operation
// https://leetcode.com/problems/design-a-stack-with-increment-operation/

import java.util.*;

class CustomStack {
    private int maxSize;
    private List<Integer> a = new ArrayList<>();

    public CustomStack(int maxSize) {
        this.maxSize = maxSize;
    }

    public void push(int x) {
        if (a.size() < maxSize) a.add(x);
    }

    public int pop() {
        if (a.isEmpty()) return -1;
        return a.remove(a.size() - 1);
    }

    public void increment(int k, int val) {
        for (int i = 0; i < Math.min(k, a.size()); i++) a.set(i, a.get(i) + val);
    }
}
