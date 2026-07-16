// LeetCode 0300 - Longest Increasing Subsequence
// https://leetcode.com/problems/longest-increasing-subsequence/

using System.Collections.Generic;

public class Solution {
    public int LengthOfLIS(int[] nums) {
        var piles = new List<int>();
        foreach (int num in nums) {
            int left = 0;
            int right = piles.Count;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (piles[mid] < num) {
                    left = mid + 1;
                } else {
                    right = mid;
                }
            }
            if (left == piles.Count) {
                piles.Add(num);
            } else {
                piles[left] = num;
            }
        }
        return piles.Count;
    }
}
