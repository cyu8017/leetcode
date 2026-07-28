// LeetCode 1033 - Moving Stones Until Consecutive
// https://leetcode.com/problems/moving-stones-until-consecutive/

using System;

public class Solution {
    public int[] NumMovesStones(int a, int b, int c) {
        int[] arr = { a, b, c };
        Array.Sort(arr);
        int x = arr[0], y = arr[1], z = arr[2];
        int minMoves;
        if (z - x == 2) minMoves = 0;
        else if (y - x <= 2 || z - y <= 2) minMoves = 1;
        else minMoves = 2;
        return new[] { minMoves, z - x - 2 };
    }
}
