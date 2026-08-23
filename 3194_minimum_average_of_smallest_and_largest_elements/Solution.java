// LeetCode 3194 - Minimum Average of Smallest and Largest Elements
// https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

import java.util.Arrays;

class Solution {
    public double minimumAverage(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        int ans = 1 << 30;
        for (int i = 0; i < n / 2; i++) ans = Math.min(ans, nums[i] + nums[n - i - 1]);
        return ans / 2.0;
    }
}
