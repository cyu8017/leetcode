// LeetCode 0857 - Minimum Cost to Hire K Workers
// https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

using System;
using System.Collections.Generic;

public class Solution {
    public double MincostToHireWorkers(int[] quality, int[] wage, int k) {
        int n = quality.Length;
        var workers = new (double ratio, int q)[n];
        for (int i = 0; i < n; i++)
            workers[i] = ((double)wage[i] / quality[i], quality[i]);
        Array.Sort(workers, (a, b) => a.ratio.CompareTo(b.ratio));
        var heap = new PriorityQueue<int, int>();
        long totalQ = 0;
        double ans = 1e18;
        foreach (var (ratio, q) in workers) {
            heap.Enqueue(q, -q);
            totalQ += q;
            if (heap.Count > k) totalQ -= heap.Dequeue();
            if (heap.Count == k) ans = Math.Min(ans, totalQ * ratio);
        }
        return ans;
    }
}
