// LeetCode 2134 - Minimum Swaps to Group All 1's Together II
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution {
    public int minSwaps(int[] nums) {
        int ones = 0;
        for (int x : nums) ones += x;
        if (ones == 0) return 0;
        int n = nums.length, window = 0;
        for (int i = 0; i < ones; i++) window += nums[i];
        int best = window;
        for (int i = 0; i < n; i++) {
            window -= nums[i];
            window += nums[(i + ones) % n];
            best = Math.max(best, window);
        }
        return ones - best;
    }
}
