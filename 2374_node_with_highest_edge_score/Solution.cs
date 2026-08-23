// LeetCode 2374 - Node With Highest Edge Score
// https://leetcode.com/problems/node-with-highest-edge-score/

public class Solution {
    public int EdgeScore(int[] edges) {
        int n = edges.Length;
        long[] score = new long[n];
        for (int i = 0; i < n; i++) score[edges[i]] += i;
        int ans = 0;
        for (int i = 1; i < n; i++)
            if (score[i] > score[ans]) ans = i;
        return ans;
    }
}
