// LeetCode 3175 - Find The First Player to win K Games in a Row
// https://leetcode.com/problems/find-the-first-player-to-win-k-games-in-a-row/

using System;

public class Solution {
    public int FindWinningPlayer(int[] skills, int k) {
        int n = skills.Length;
        k = Math.Min(k, n - 1);
        int i = 0, cnt = 0;
        for (int j = 1; j < n; j++) {
            if (skills[i] < skills[j]) { i = j; cnt = 1; }
            else cnt++;
            if (cnt == k) break;
        }
        return i;
    }
}
