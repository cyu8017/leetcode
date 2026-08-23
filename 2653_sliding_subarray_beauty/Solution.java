// LeetCode 2653 - Sliding Subarray Beauty
// https://leetcode.com/problems/sliding-subarray-beauty/

class Solution {
    public int[] getSubarrayBeauty(int[] nums, int k, int x) {
        int[] freq = new int[101];
        int[] ans = new int[nums.length - k + 1];
        for (int i = 0; i < nums.length; i++) {
            freq[nums[i] + 50]++;
            if (i >= k) freq[nums[i - k] + 50]--;
            if (i >= k - 1) {
                int need = x, val = 0;
                for (int j = 0; j < 50; j++) {
                    need -= freq[j];
                    if (need <= 0) {
                        val = j - 50;
                        break;
                    }
                }
                ans[i - k + 1] = val;
            }
        }
        return ans;
    }
}
