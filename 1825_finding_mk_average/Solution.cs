// LeetCode 1825 - Finding MK Average
// https://leetcode.com/problems/finding-mk-average/

using System;
using System.Collections.Generic;

public class MKAverage {
    private readonly int m;
    private readonly int k;
    private readonly Queue<int> stream = new();

    public MKAverage(int m, int k) {
        this.m = m;
        this.k = k;
    }

    public void AddElement(int num) {
        stream.Enqueue(num);
        if (stream.Count > m) stream.Dequeue();
    }

    public int CalculateMKAverage() {
        if (stream.Count < m) return -1;
        var window = stream.ToArray();
        Array.Sort(window);
        long sum = 0;
        for (int i = k; i < window.Length - k; i++) sum += window[i];
        return (int)(sum / (window.Length - 2 * k));
    }
}
