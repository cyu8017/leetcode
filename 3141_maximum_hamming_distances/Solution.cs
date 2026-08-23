// LeetCode 3141 - Maximum Hamming Distances
// https://leetcode.com/problems/maximum-hamming-distances/

using System.Collections.Generic;

public class Solution {
    public int[] MaxHammingDistances(int[] nums, int m) {
        int[] dist = new int[1 << m];
        for (int i = 0; i < dist.Length; i++) dist[i] = -1;
        var q = new List<int>();
        foreach (int x in nums) {
            dist[x] = 0;
            q.Add(x);
        }
        for (int k = 1; q.Count > 0; k++) {
            var t = new List<int>();
            foreach (int x in q) {
                for (int i = 0; i < m; i++) {
                    int y = x ^ (1 << i);
                    if (dist[y] == -1) {
                        dist[y] = k;
                        t.Add(y);
                    }
                }
            }
            q = t;
        }
        for (int i = 0; i < nums.Length; i++) {
            int x = nums[i];
            nums[i] = m - dist[x ^ ((1 << m) - 1)];
        }
        return nums;
    }
}
