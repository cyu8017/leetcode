// LeetCode 0997 - Find the Town Judge
// https://leetcode.com/problems/find-the-town-judge/

class Solution {
    public int findJudge(int n, int[][] trust) {
        int[] score = new int[n + 1];
        for (int[] t : trust) {
            score[t[0]]--;
            score[t[1]]++;
        }
        for (int i = 1; i <= n; i++) if (score[i] == n - 1) return i;
        return -1;
    }
}
