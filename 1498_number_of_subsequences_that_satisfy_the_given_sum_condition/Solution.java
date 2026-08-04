// LeetCode 1498 - Number Of Subsequences That Satisfy The Given Sum Condition
// https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

import java.util.*;

class Solution {
    public int numSubseq(int[] nums, int target) {
        Arrays.sort(nums);
        int mod = 1000000007, left = 0, right = nums.length - 1, ans = 0;
        var powers = new int[nums.length + 1]; powers[0] = 1;
        for (int i = 1; i < powers.length; i++) powers[i] = powers[i - 1] * 2 % mod;
        while (left <= right) {
            if (nums[left] + nums[right] <= target) { ans = (ans + powers[right - left]) % mod; left++; }
            else right--;
        }
        return ans;
    }
}
