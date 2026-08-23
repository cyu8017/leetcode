// LeetCode 3522 - Calculate Score After Performing Instructions
// https://leetcode.com/problems/calculate-score-after-performing-instructions/

class Solution {
    public long calculateScore(String[] instructions, int[] values) {
        int n = values.length;
        boolean[] vis = new boolean[n];
        long ans = 0;
        int i = 0;
        while (i >= 0 && i < n && !vis[i]) {
            vis[i] = true;
            if (instructions[i].charAt(0) == 'a') {
                ans += values[i];
                i += 1;
            } else {
                i += values[i];
            }
        }
        return ans;
    }
}
