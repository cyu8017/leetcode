// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

import java.util.*;

class Solution {
    public int minPushBox(char[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[] box = null, player = null, target = null;
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 'B') box = new int[] {r, c};
                else if (grid[r][c] == 'S') player = new int[] {r, c};
                else if (grid[r][c] == 'T') target = new int[] {r, c};
            }
        }

        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        HashSet<Long> seen = new HashSet<>();
        queue.add(new int[] {box[0], box[1], player[0], player[1], 0});
        seen.add(stateKey(box[0], box[1], player[0], player[1], n));

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int br = cur[0], bc = cur[1], pr = cur[2], pc = cur[3], pushes = cur[4];
            if (br == target[0] && bc == target[1]) return pushes;
            Set<Integer> canReach = reachable(grid, m, n, pr, pc, br, bc);
            for (int[] d : dirs) {
                int sr = br - d[0], sc = bc - d[1];
                int nbr = br + d[0], nbc = bc + d[1];
                if (!canReach.contains(sr * n + sc)) continue;
                if (nbr < 0 || nbr >= m || nbc < 0 || nbc >= n || grid[nbr][nbc] == '#') continue;
                long key = stateKey(nbr, nbc, br, bc, n);
                if (seen.add(key)) queue.add(new int[] {nbr, nbc, br, bc, pushes + 1});
            }
        }
        return -1;
    }

    private long stateKey(int br, int bc, int pr, int pc, int n) {
        return ((long) br * n + bc) << 20 | (pr * n + pc);
    }

    private Set<Integer> reachable(char[][] grid, int m, int n, int pr, int pc, int br, int bc) {
        Set<Integer> seen = new HashSet<>();
        ArrayDeque<int[]> stack = new ArrayDeque<>();
        stack.push(new int[] {pr, pc});
        seen.add(pr * n + pc);
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            for (int[] d : dirs) {
                int nr = cur[0] + d[0], nc = cur[1] + d[1];
                int key = nr * n + nc;
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == '#') continue;
                if (nr == br && nc == bc) continue;
                if (seen.add(key)) stack.push(new int[] {nr, nc});
            }
        }
        return seen;
    }
}
