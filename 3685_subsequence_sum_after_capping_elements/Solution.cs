// LeetCode 3685 - Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/

using System;

public class Solution {
    public bool[] SubsequenceSumAfterCapping(int[] nums, int k) {
        int n = nums.Length;
        int[] sorted = (int[])nums.Clone();
        Array.Sort(sorted);
        bool[] ans = new bool[n], reach = new bool[k + 1];
        reach[0] = true;
        int idx = 0;
        for (int x = 1; x <= n; x++) {
            while (idx < n && sorted[idx] <= x) {
                int v = sorted[idx];
                for (int s = k; s >= v; s--) {
                    if (reach[s - v]) reach[s] = true;
                }
                idx++;
            }
            bool[] tmp = (bool[])reach.Clone();
            int rem = n - idx;
            for (int s = 0; s <= k; s++) {
                if (!reach[s]) continue;
                for (int t = 1; t <= rem && s + t * x <= k; t++) tmp[s + t * x] = true;
            }
            ans[x - 1] = tmp[k];
        }
        return ans;
    }
}
