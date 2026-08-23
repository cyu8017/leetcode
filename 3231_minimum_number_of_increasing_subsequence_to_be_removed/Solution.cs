// LeetCode 3231 - Minimum Number of Increasing Subsequence to Be Removed
// https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

using System.Collections.Generic;

public class Solution {
    public int MinOperations(int[] nums) {
        var g = new List<int>();
        foreach (int x in nums) {
            int l = 0, r = g.Count;
            while (l < r) {
                int mid = (l + r) >> 1;
                if (g[mid] < x) r = mid;
                else l = mid + 1;
            }
            if (l == g.Count) g.Add(x);
            else g[l] = x;
        }
        return g.Count;
    }
}
