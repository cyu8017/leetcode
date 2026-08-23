// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

using System;

public class Solution {
    public long MinOperations(int[] nums, int k) {
        int n = nums.Length;
        long ans = 1L << 62;
        for (int i = 0; i + k <= n; i++) {
            int[] sub = new int[k];
            Array.Copy(nums, i, sub, 0, k);
            Array.Sort(sub);
            int med = sub[k / 2];
            long cost = 0;
            foreach (int x in sub) cost += Math.Abs(x - med);
            if (cost < ans) ans = cost;
        }
        return ans;
    }
}
