// LeetCode 3357 - Minimize the Maximum Adjacent Element Difference
// https://leetcode.com/problems/minimize-the-maximum-adjacent-element-difference/

using System;

public class Solution {
    public int MinDifference(int[] nums) {
        int n = nums.Length;
        bool Ok(int d) {
            int prev = -1;
            for (int i = 0; i < n; i++) {
                if (nums[i] != -1) {
                    if (prev != -1 && Math.Abs(nums[i] - prev) > d) return false;
                    prev = nums[i];
                    continue;
                }
                int j = i;
                while (j < n && nums[j] == -1) j++;
                int left = prev;
                int right = (j < n) ? nums[j] : -1;
                int gap = j - i;
                if (left == -1 && right == -1) return true;
                if (left == -1 || right == -1) {
                    prev = -1;
                    i = j - 1;
                    continue;
                }
                if (Math.Abs(left - right) > d * (gap + 1)) return false;
                prev = -1;
                i = j - 1;
            }
            return true;
        }
        int lo = 0, hi = 1000000000;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (Ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
