// LeetCode 3362 - Zero Array Transformation III
// https://leetcode.com/problems/zero-array-transformation-iii/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaxRemoval(int[] nums, int[][] queries) {
        Array.Sort(queries, (a, b) => a[0].CompareTo(b[0]));
        var h = new PriorityQueue<int, int>();
        int n = nums.Length;
        int[] diff = new int[n + 1];
        int j = 0, used = 0, cur = 0;
        for (int i = 0; i < n; i++) {
            cur += diff[i];
            while (j < queries.Length && queries[j][0] == i) {
                h.Enqueue(queries[j][1], -queries[j][1]);
                j++;
            }
            while (cur < nums[i]) {
                if (h.Count == 0 || h.Peek() < i) return -1;
                int r = h.Dequeue();
                cur++;
                diff[r + 1]--;
                used++;
            }
        }
        return queries.Length - used;
    }
}
