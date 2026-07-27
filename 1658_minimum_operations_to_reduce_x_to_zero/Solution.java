// LeetCode 1658 - Minimum Operations to Reduce X to Zero
// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

class Solution {
    public int minOperations(int[] nums, int x) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }
        int target = total - x;
        if (target < 0) {
            return -1;
        }
        int best = -1;
        int left = 0;
        int cur = 0;
        for (int right = 0; right < nums.length; right++) {
            cur += nums[right];
            while (cur > target) {
                cur -= nums[left++];
            }
            if (cur == target) {
                best = Math.max(best, right - left + 1);
            }
        }
        return best < 0 ? -1 : nums.length - best;
    }
}
