// LeetCode 1040 - Moving Stones Until Consecutive II
// https://leetcode.com/problems/moving-stones-until-consecutive-ii/

using System;

public class Solution {
    public int[] NumMovesStonesII(int[] stones) {
        Array.Sort(stones);
        int n = stones.Length;
        int maxMoves = Math.Max(stones[n - 1] - stones[1] - n + 2, stones[n - 2] - stones[0] - n + 2);
        int minMoves = maxMoves, i = 0;
        for (int j = 0; j < n; j++) {
            while (stones[j] - stones[i] + 1 > n) i++;
            int inside = j - i + 1;
            if (inside == n - 1 && stones[j] - stones[i] + 1 == n - 1)
                minMoves = Math.Min(minMoves, 2);
            else
                minMoves = Math.Min(minMoves, n - inside);
        }
        return new[] { minMoves, maxMoves };
    }
}
