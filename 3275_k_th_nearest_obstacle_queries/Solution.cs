// LeetCode 3275 - K-th Nearest Obstacle Queries
// https://leetcode.com/problems/k-th-nearest-obstacle-queries/

using System;
using System.Collections.Generic;

public class Solution {
    public int[] ResultsArray(int[][] queries, int k) {
        var h = new PriorityQueue<int, int>();
        int[] ans = new int[queries.Length];
        for (int i = 0; i < queries.Length; i++) {
            int d = Math.Abs(queries[i][0]) + Math.Abs(queries[i][1]);
            h.Enqueue(d, -d);
            if (h.Count > k) h.Dequeue();
            ans[i] = h.Count < k ? -1 : h.Peek();
        }
        return ans;
    }
}
