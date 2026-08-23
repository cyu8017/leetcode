// LeetCode 0716 - Max Stack
// https://leetcode.com/problems/max-stack/

using System;
using System.Collections.Generic;

public class MaxStack {
    private readonly List<int> stack = new List<int>();
    private readonly List<int> maxes = new List<int>();
    public MaxStack() { }

    public void Push(int x) {
        stack.Add(x);
        maxes.Add(maxes.Count == 0 ? x : Math.Max(x, maxes[maxes.Count - 1]));
    }

    public int Pop() {
        maxes.RemoveAt(maxes.Count - 1);
        int val = stack[stack.Count - 1];
        stack.RemoveAt(stack.Count - 1);
        return val;
    }

    public int Top() => stack[stack.Count - 1];
    public int PeekMax() => maxes[maxes.Count - 1];

    public int PopMax() {
        int maxVal = PeekMax();
        var buffer = new List<int>();
        while (Top() != maxVal) buffer.Add(Pop());
        Pop();
        for (int i = buffer.Count - 1; i >= 0; i--) Push(buffer[i]);
        return maxVal;
    }
}
