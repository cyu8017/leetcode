// LeetCode 0895 - Maximum Frequency Stack
// https://leetcode.com/problems/maximum-frequency-stack/

using System;
using System.Collections.Generic;

public class FreqStack {
    private readonly Dictionary<int, int> freq = new();
    private readonly Dictionary<int, List<int>> group = new();
    private int maxfreq;

    public FreqStack() {
        maxfreq = 0;
    }

    public void Push(int val) {
        if (!freq.ContainsKey(val)) freq[val] = 0;
        int f = ++freq[val];
        maxfreq = Math.Max(maxfreq, f);
        if (!group.ContainsKey(f)) group[f] = new List<int>();
        group[f].Add(val);
    }

    public int Pop() {
        var list = group[maxfreq];
        int val = list[list.Count - 1];
        list.RemoveAt(list.Count - 1);
        freq[val]--;
        if (list.Count == 0) maxfreq--;
        return val;
    }
}
