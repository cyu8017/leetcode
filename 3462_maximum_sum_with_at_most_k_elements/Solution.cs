// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

using System;
using System.Collections.Generic;

public class Solution {
    public long MaxSum(int[][] grid, int[] limits, int k) {
        var h = new PriorityQueue<int, int>();
        long sum = 0;
        for (int i = 0; i < grid.Length; i++) {
            int[] r = (int[])grid[i].Clone();
            Array.Sort(r, (a, b) => b.CompareTo(a));
            int lim = limits[i];
            if (lim > r.Length) lim = r.Length;
            for (int j = 0; j < lim; j++) {
                h.Enqueue(r[j], r[j]);
                sum += r[j];
                if (h.Count > k) {
                    sum -= h.Dequeue();
                }
            }
        }
        return sum;
    }
}
