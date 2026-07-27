// LeetCode 1674 - Minimum Moves to Make Array Complementary
// https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

class Solution {
    public int minMoves(int[] nums, int limit) {
        int n = nums.length;
        int[] diff = new int[2 * limit + 2];
        for (int i = 0; i < n / 2; i++) {
            int a = nums[i];
            int b = nums[n - 1 - i];
            int lo = Math.min(a, b) + 1;
            int hi = Math.max(a, b) + limit;
            int s = a + b;
            diff[2] += 2;
            diff[lo] -= 1;
            diff[s] -= 1;
            diff[s + 1] += 1;
            diff[hi + 1] += 1;
        }
        int ans = Integer.MAX_VALUE;
        int cur = 0;
        for (int s = 2; s <= 2 * limit; s++) {
            cur += diff[s];
            ans = Math.min(ans, cur);
        }
        return ans;
    }
}
