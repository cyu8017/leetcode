// LeetCode 2134 - Minimum Swaps to Group All 1's Together II
// https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

public class Solution {
    public int MinSwaps(int[] nums) {
        int ones = 0;
        foreach (int x in nums) ones += x;
        if (ones == 0) return 0;
        int n = nums.Length, window = 0;
        for (int i = 0; i < ones; i++) window += nums[i];
        int best = window;
        for (int i = 0; i < n; i++) {
            window -= nums[i];
            window += nums[(i + ones) % n];
            best = Math.Max(best, window);
        }
        return ones - best;
    }
}
