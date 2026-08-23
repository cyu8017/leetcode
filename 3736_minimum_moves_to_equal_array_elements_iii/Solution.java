// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

class Solution {
    public int minMoves(int[] nums) {
        int mx = 0, s = 0;
        for (int x : nums) {
            mx = Math.max(mx, x);
            s += x;
        }
        return mx * nums.length - s;
    }
}
