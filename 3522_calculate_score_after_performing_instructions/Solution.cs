// LeetCode 3522 - Calculate Score After Performing Instructions
// https://leetcode.com/problems/calculate-score-after-performing-instructions/

public class Solution {
    public long CalculateScore(string[] instructions, int[] values) {
        int n = values.Length;
        bool[] vis = new bool[n];
        long ans = 0;
        int i = 0;
        while (i >= 0 && i < n && !vis[i]) {
            vis[i] = true;
            if (instructions[i][0] == 'a') {
                ans += values[i];
                i += 1;
            } else {
                i += values[i];
            }
        }
        return ans;
    }
}
