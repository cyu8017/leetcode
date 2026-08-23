// LeetCode 2616 - Minimize the Maximum Difference of Pairs
// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

using System;

public class Solution {
    public int MinimizeMax(int[] nums, int p) {
        Array.Sort(nums);
        bool Ok(int d) {
            int cnt = 0;
            for (int i = 0; i + 1 < nums.Length;) {
                if (nums[i + 1] - nums[i] <= d) {
                    cnt++;
                    i += 2;
                } else {
                    i++;
                }
            }
            return cnt >= p;
        }
        int lo = 0, hi = nums[^1] - nums[0];
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (Ok(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
