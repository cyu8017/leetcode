// LeetCode 0699 - Falling Squares
// https://leetcode.com/problems/falling-squares/

using System;
using System.Collections.Generic;

public class Solution {
    public IList<int> FallingSquares(int[][] positions) {
        var intervals = new List<(int l, int r, int height)>();
        var answer = new List<int>();
        int maxHeight = 0;
        foreach (var pos in positions) {
            int left = pos[0], side = pos[1], right = left + side, bas = 0;
            foreach (var it in intervals) {
                if (it.r > left && it.l < right) bas = Math.Max(bas, it.height);
            }
            int height = bas + side;
            intervals.Add((left, right, height));
            maxHeight = Math.Max(maxHeight, height);
            answer.Add(maxHeight);
        }
        return answer;
    }
}
