// LeetCode 0887 - Super Egg Drop
// https://leetcode.com/problems/super-egg-drop/

class Solution {
    public int superEggDrop(int k, int n) {
        int[] dp = new int[k + 1];
        int moves = 0;
        while (dp[k] < n) {
            moves++;
            for (int eggs = k; eggs >= 1; eggs--) {
                dp[eggs] = dp[eggs] + dp[eggs - 1] + 1;
            }
        }
        return moves;
    }
}
