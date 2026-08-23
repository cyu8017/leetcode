// LeetCode 3257 - Maximum Value Sum by Placing Three Rooks II
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/

using System.Collections.Generic;

public class Solution {
    struct Cell { public int v, c; public Cell(int v, int c) { this.v = v; this.c = c; } }

    public long MaximumValueSum(int[][] board) {
        int m = board.Length, n = board[0].Length;
        var tops = new List<Cell>[m];
        for (int i = 0; i < m; i++) {
            var row = new List<Cell>();
            for (int j = 0; j < n; j++) {
                var cur = new Cell(board[i][j], j);
                bool placed = false;
                for (int t = 0; t < row.Count; t++) {
                    if (cur.v > row[t].v) {
                        row.Insert(t, cur);
                        placed = true;
                        break;
                    }
                }
                if (!placed) row.Add(cur);
                if (row.Count > 3) row.RemoveRange(3, row.Count - 3);
            }
            tops[i] = row;
        }
        long ans = -(1L << 62);
        for (int i = 0; i < m; i++) {
            foreach (var a in tops[i]) {
                for (int j = i + 1; j < m; j++) {
                    foreach (var b in tops[j]) {
                        if (a.c == b.c) continue;
                        for (int k = j + 1; k < m; k++) {
                            foreach (var c in tops[k]) {
                                if (c.c == a.c || c.c == b.c) continue;
                                long s = (long)a.v + b.v + c.v;
                                if (s > ans) ans = s;
                            }
                        }
                    }
                }
            }
        }
        return ans;
    }
}
