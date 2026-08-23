// LeetCode 3552 - Grid Teleportation Traversal
// https://leetcode.com/problems/grid-teleportation-traversal/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public int minMoves(String[] matrix) {
        int m = matrix.length, n = matrix[0].length();
        Map<Character, List<int[]>> g = new HashMap<>();
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                if (Character.isLetter(matrix[i].charAt(j)))
                    g.computeIfAbsent(matrix[i].charAt(j), k -> new ArrayList<>()).add(new int[] {i, j});
        int[] dirs = {-1, 0, 1, 0, -1};
        final int INF = 1 << 30;
        int[][] dist = new int[m][n];
        for (int i = 0; i < m; i++) java.util.Arrays.fill(dist[i], INF);
        dist[0][0] = 0;
        Deque<int[]> q = new ArrayDeque<>();
        q.add(new int[] {0, 0});
        while (!q.isEmpty()) {
            int[] cur = q.pollFirst();
            int i = cur[0], j = cur[1], d = dist[i][j];
            if (i == m - 1 && j == n - 1) return d;
            char c = matrix[i].charAt(j);
            if (g.containsKey(c)) {
                for (int[] p : g.get(c)) {
                    int x = p[0], y = p[1];
                    if (d < dist[x][y]) {
                        dist[x][y] = d;
                        q.addFirst(new int[] {x, y});
                    }
                }
                g.remove(c);
            }
            for (int idx = 0; idx < 4; idx++) {
                int x = i + dirs[idx], y = j + dirs[idx + 1];
                if (0 <= x && x < m && 0 <= y && y < n && matrix[x].charAt(y) != '#' && d + 1 < dist[x][y]) {
                    dist[x][y] = d + 1;
                    q.addLast(new int[] {x, y});
                }
            }
        }
        return -1;
    }
}
