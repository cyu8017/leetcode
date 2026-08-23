// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

import java.util.Arrays;

class Solution {
    public long perfectPairs(int[] nums) {
        int n = nums.length;
        int[] absNums = new int[n];
        for (int i = 0; i < n; i++) absNums[i] = Math.abs(nums[i]);
        Arrays.sort(absNums);
        long ans = 0;
        int j = 0;
        for (int i = 0; i < n; i++) {
            if (j < i + 1) j = i + 1;
            while (j < n && absNums[j] <= 2 * absNums[i]) j++;
            ans += j - i - 1;
        }
        return ans;
    }
}
