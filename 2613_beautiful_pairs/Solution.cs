// LeetCode 2613 - Beautiful Pairs
// https://leetcode.com/problems/beautiful-pairs/

using System;

public class Solution {
    public int[] BeautifulPair(int[] nums1, int[] nums2) {
        int n = nums1.Length;
        long bestDist = long.MaxValue / 4;
        int[] ans = { 0, 1 };
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                long d = Math.Abs(nums1[i] - nums1[j]) + Math.Abs(nums2[i] - nums2[j]);
                if (d < bestDist || (d == bestDist && (i < ans[0] || (i == ans[0] && j < ans[1])))) {
                    bestDist = d;
                    ans = new[] { i, j };
                }
            }
        }
        return ans;
    }
}
