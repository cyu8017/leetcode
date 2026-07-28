// LeetCode 1033 - Moving Stones Until Consecutive
// https://leetcode.com/problems/moving-stones-until-consecutive/

import java.util.Arrays;

class Solution {
    public int[] numMovesStones(int a, int b, int c) {
        int[] arr = {a, b, c};
        Arrays.sort(arr);
        int x = arr[0], y = arr[1], z = arr[2];
        int minMoves = 2;
        if (z - x == 2) minMoves = 0;
        else if (y - x <= 2 || z - y <= 2) minMoves = 1;
        return new int[]{minMoves, z - x - 2};
    }
}
