// LeetCode 3034 - Number of Subarrays That Match a Pattern I
// https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/

class Solution {
    private int f(int a, int b) {
        if (a == b) return 0;
        return a < b ? 1 : -1;
    }

    public int countMatchingSubarrays(int[] nums, int[] pattern) {
        int n = nums.length, m = pattern.length, ans = 0;
        for (int i = 0; i < n - m; i++) {
            int ok = 1;
            for (int k = 0; k < m && ok != 0; k++)
                if (f(nums[i + k], nums[i + k + 1]) != pattern[k]) ok = 0;
            ans += ok;
        }
        return ans;
    }
}
