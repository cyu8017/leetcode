// LeetCode 1381 - Design A Stack With Increment Operation
// https://leetcode.com/problems/design-a-stack-with-increment-operation/

using System.Collections.Generic;
public class CustomStack {
    int maxSize; List<int> a = new List<int>();
    public CustomStack(int maxSize) { this.maxSize = maxSize; }
    public void Push(int x) { if (a.Count < maxSize) a.Add(x); }
    public int Pop() {
        if (a.Count == 0) return -1;
        int v = a[a.Count - 1]; a.RemoveAt(a.Count - 1); return v;
    }
    public void Increment(int k, int val) {
        for (int i = 0; i < System.Math.Min(k, a.Count); i++) a[i] += val;
    }
}
