// LeetCode 3254 - Find the Power of K-Size Subarrays I
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

class Solution {
    public int[] resultsArray(int[] nums, int k) {
        int n = nums.length;
        int[] ans = new int[n - k + 1];
        for (int i = 0; i <= n - k; i++) {
            boolean ok = true;
            for (int j = i + 1; j < i + k; j++) {
                if (nums[j] != nums[j - 1] + 1) { ok = false; break; }
            }
            ans[i] = ok ? nums[i + k - 1] : -1;
        }
        return ans;
    }
}
