// LeetCode 0795 - Number of Subarrays with Bounded Maximum
// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

public class Solution {
    public int NumSubarrayBoundedMax(int[] nums, int left, int right) {
        return CountAtMost(nums, right) - CountAtMost(nums, left - 1);
    }

    private int CountAtMost(int[] nums, int bound) {
        int ans = 0, cur = 0;
        foreach (int num in nums) {
            if (num <= bound) { cur++; ans += cur; }
            else cur = 0;
        }
        return ans;
    }
}
