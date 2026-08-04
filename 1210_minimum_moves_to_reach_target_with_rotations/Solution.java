// LeetCode 1210 - Minimum Moves to Reach Target With Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

import java.util.*;

class Solution {
    public int minimumMoves(int[][] grid) {
        int n = grid.length;
        int[] start = {0, 0, 0};
        int[] target = {n - 1, n - 2, 0};
        ArrayDeque<int[]> q = new ArrayDeque<>();
        q.add(new int[] {start[0], start[1], start[2], 0});
        Set<String> seen = new HashSet<>();
        seen.add(key(start[0], start[1], start[2]));
        while (!q.isEmpty()) {
            int[] cur = q.removeFirst();
            int r = cur[0];
            int c = cur[1];
            int orient = cur[2];
            int moves = cur[3];
            if (r == target[0] && c == target[1] && orient == target[2]) return moves;
            List<int[]> next = new ArrayList<>();
            if (orient == 0) {
                if (c + 2 < n && grid[r][c + 2] == 0) next.add(new int[] {r, c + 1, 0});
                if (r + 1 < n && grid[r + 1][c] == 0 && grid[r + 1][c + 1] == 0) {
                    next.add(new int[] {r + 1, c, 0});
                    next.add(new int[] {r, c, 1});
                }
            } else {
                if (r + 2 < n && grid[r + 2][c] == 0) next.add(new int[] {r + 1, c, 1});
                if (c + 1 < n && grid[r][c + 1] == 0 && grid[r + 1][c + 1] == 0) {
                    next.add(new int[] {r, c + 1, 1});
                    next.add(new int[] {r, c, 0});
                }
            }
            for (int[] state : next) {
                String k = key(state[0], state[1], state[2]);
                if (seen.add(k)) {
                    q.add(new int[] {state[0], state[1], state[2], moves + 1});
                }
            }
        }
        return -1;
    }

    private String key(int r, int c, int orient) {
        return r + "," + c + "," + orient;
    }
}
