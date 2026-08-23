// LeetCode 3865 - Reverse K Subarrays
// https://leetcode.com/problems/reverse-k-subarrays/

class Solution {
    public int[] reverseSubarrays(int[] nums, int k) {
        int n = nums.length;
        int m = n / k;
        for (int i = 0; i < n; i += m) {
            int lo = i, hi = i + m - 1;
            while (lo < hi) {
                int t = nums[lo];
                nums[lo] = nums[hi];
                nums[hi] = t;
                lo++;
                hi--;
            }
        }
        return nums;
    }
}
