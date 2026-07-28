// LeetCode 1040 - Moving Stones Until Consecutive II
// https://leetcode.com/problems/moving-stones-until-consecutive-ii/

import java.util.Arrays;

class Solution {
    public int[] numMovesStonesII(int[] stones) {
        Arrays.sort(stones);
        int n = stones.length;
        int maxMoves = Math.max(stones[n - 1] - stones[1] - n + 2, stones[n - 2] - stones[0] - n + 2);
        int minMoves = maxMoves, i = 0;
        for (int j = 0; j < n; j++) {
            while (stones[j] - stones[i] + 1 > n) i++;
            int inside = j - i + 1;
            int cur = n - inside;
            if (inside == n - 1 && stones[j] - stones[i] + 1 == n - 1) cur = 2;
            minMoves = Math.min(minMoves, cur);
        }
        return new int[]{minMoves, maxMoves};
    }
}
