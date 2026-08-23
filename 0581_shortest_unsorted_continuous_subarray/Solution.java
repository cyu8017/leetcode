// LeetCode 0581 - Shortest Unsorted Continuous Subarray
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int n = nums.length;
        int left = -1;
        int right = -2;
        int maxSeen = nums[0];
        int minSeen = nums[n - 1];
        for (int i = 0; i < n; ++i) {
            maxSeen = Math.max(maxSeen, nums[i]);
            if (nums[i] < maxSeen) {
                right = i;
            }
            int j = n - 1 - i;
            minSeen = Math.min(minSeen, nums[j]);
            if (nums[j] > minSeen) {
                left = j;
            }
        }
        return right - left + 1;
    }
}
