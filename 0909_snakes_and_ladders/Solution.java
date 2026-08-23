// LeetCode 0909 - Snakes and Ladders
// https://leetcode.com/problems/snakes-and-ladders/

import java.util.*;

class Solution {
    public int snakesAndLadders(int[][] board) {
        int n = board.length;
        int target = n * n;
        Queue<Integer> q = new ArrayDeque<>();
        boolean[] seen = new boolean[target + 1];
        q.offer(1);
        seen[1] = true;
        int moves = 0;
        while (!q.isEmpty()) {
            int sz = q.size();
            for (int s = 0; s < sz; s++) {
                int cur = q.poll();
                if (cur == target) return moves;
                int lim = Math.min(cur + 6, target);
                for (int nxt = cur + 1; nxt <= lim; nxt++) {
                    int[] rc = pos(nxt, n);
                    int dest = board[rc[0]][rc[1]] != -1 ? board[rc[0]][rc[1]] : nxt;
                    if (!seen[dest]) {
                        seen[dest] = true;
                        q.offer(dest);
                    }
                }
            }
            moves++;
        }
        return -1;
    }

    private int[] pos(int square, int n) {
        square--;
        int row = square / n;
        int rem = square % n;
        int r = n - 1 - row;
        int c = (row % 2 == 0) ? rem : n - 1 - rem;
        return new int[] {r, c};
    }
}
