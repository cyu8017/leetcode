// LeetCode 2895 - Minimum Processing Time
// https://leetcode.com/problems/minimum-processing-time/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinProcessingTime(IList<int> processorTime, IList<int> tasks) {
        var pt = new List<int>(processorTime);
        var tk = new List<int>(tasks);
        pt.Sort();
        tk.Sort((a, b) => b.CompareTo(a));
        int ans = 0;
        for (int i = 0; i < pt.Count; i++) {
            int fin = pt[i] + tk[i * 4];
            if (fin > ans) ans = fin;
        }
        return ans;
    }
}
