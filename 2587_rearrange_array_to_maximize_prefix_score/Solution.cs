// LeetCode 2587 - Rearrange Array to Maximize Prefix Score
// https://leetcode.com/problems/rearrange-array-to-maximize-prefix-score/

using System;

public class Solution {
    public int MaxScore(int[] nums) {
        Array.Sort(nums, (a, b) => b.CompareTo(a));
        long sum = 0;
        int ans = 0;
        foreach (int x in nums) {
            sum += x;
            if (sum > 0) ans++;
            else break;
        }
        return ans;
    }
}
