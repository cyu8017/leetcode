// LeetCode 3256 - Maximum Value Sum by Placing Three Rooks I
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/

import java.util.ArrayList;
import java.util.List;

class Solution {
    private static class Cell {
        int v, c;
        Cell(int v, int c) { this.v = v; this.c = c; }
    }

    public long maximumValueSum(int[][] board) {
        int m = board.length, n = board[0].length;
        List<List<Cell>> tops = new ArrayList<>();
        for (int i = 0; i < m; i++) {
            List<Cell> row = new ArrayList<>();
            for (int j = 0; j < n; j++) {
                Cell cur = new Cell(board[i][j], j);
                boolean placed = false;
                for (int t = 0; t < row.size(); t++) {
                    if (cur.v > row.get(t).v) {
                        row.add(t, cur);
                        placed = true;
                        break;
                    }
                }
                if (!placed) row.add(cur);
                if (row.size() > 3) row.subList(3, row.size()).clear();
            }
            tops.add(row);
        }
        long ans = -(1L << 62);
        for (int i = 0; i < m; i++) {
            for (Cell a : tops.get(i)) {
                for (int j = i + 1; j < m; j++) {
                    for (Cell b : tops.get(j)) {
                        if (a.c == b.c) continue;
                        for (int k = j + 1; k < m; k++) {
                            for (Cell c : tops.get(k)) {
                                if (c.c == a.c || c.c == b.c) continue;
                                long s = (long) a.v + b.v + c.v;
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
