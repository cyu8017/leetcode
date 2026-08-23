// LeetCode 0795 - Number of Subarrays with Bounded Maximum
// https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

class Solution {
    public int numSubarrayBoundedMax(int[] nums, int left, int right) {
        return countAtMost(nums, right) - countAtMost(nums, left - 1);
    }

    private int countAtMost(int[] nums, int bound) {
        int ans = 0, cur = 0;
        for (int num : nums) {
            if (num <= bound) {
                cur++;
                ans += cur;
            } else {
                cur = 0;
            }
        }
        return ans;
    }
}
