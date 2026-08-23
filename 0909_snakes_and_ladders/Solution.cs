// LeetCode 0909 - Snakes and Ladders
// https://leetcode.com/problems/snakes-and-ladders/

using System;
using System.Collections.Generic;

public class Solution {
    public int SnakesAndLadders(int[][] board) {
        int n = board.Length;
        int target = n * n;
        (int r, int c) Pos(int square) {
            square--;
            int row = square / n;
            int rem = square % n;
            int r = n - 1 - row;
            int c = (row % 2 == 0) ? rem : n - 1 - rem;
            return (r, c);
        }
        var q = new Queue<int>();
        bool[] seen = new bool[target + 1];
        q.Enqueue(1);
        seen[1] = true;
        int moves = 0;
        while (q.Count > 0) {
            int sz = q.Count;
            for (int s = 0; s < sz; s++) {
                int cur = q.Dequeue();
                if (cur == target) return moves;
                int lim = Math.Min(cur + 6, target);
                for (int nxt = cur + 1; nxt <= lim; nxt++) {
                    var (r, c) = Pos(nxt);
                    int dest = board[r][c] != -1 ? board[r][c] : nxt;
                    if (!seen[dest]) {
                        seen[dest] = true;
                        q.Enqueue(dest);
                    }
                }
            }
            moves++;
        }
        return -1;
    }
}
