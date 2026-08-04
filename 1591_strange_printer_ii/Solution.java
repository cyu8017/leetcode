// LeetCode 1591 - Strange Printer II
// https://leetcode.com/problems/strange-printer-ii/

import java.util.*;

class Solution {
    public boolean isPrintable(int[][] targetGrid) {
        Set<Integer> colors = new HashSet<>();
        Map<Integer, int[]> bounds = new HashMap<>();
        for (int r = 0; r < targetGrid.length; r++) {
            for (int col = 0; col < targetGrid[r].length; col++) {
                int c = targetGrid[r][col];
                colors.add(c);
                int[] b = bounds.get(c);
                if (b == null) {
                    bounds.put(c, new int[]{r, col, r, col});
                } else {
                    b[0] = Math.min(b[0], r);
                    b[1] = Math.min(b[1], col);
                    b[2] = Math.max(b[2], r);
                    b[3] = Math.max(b[3], col);
                }
            }
        }
        Map<Integer, Set<Integer>> graph = new HashMap<>();
        Map<Integer, Integer> indegree = new HashMap<>();
        for (int c : colors) {
            graph.put(c, new HashSet<>());
            indegree.put(c, 0);
        }
        for (Map.Entry<Integer, int[]> entry : bounds.entrySet()) {
            int c = entry.getKey();
            int[] b = entry.getValue();
            for (int r = b[0]; r <= b[2]; r++) {
                for (int col = b[1]; col <= b[3]; col++) {
                    int other = targetGrid[r][col];
                    if (other != c && graph.get(c).add(other)) {
                        indegree.put(other, indegree.get(other) + 1);
                    }
                }
            }
        }
        Queue<Integer> queue = new ArrayDeque<>();
        for (int c : colors) {
            if (indegree.get(c) == 0) {
                queue.add(c);
            }
        }
        int seen = 0;
        while (!queue.isEmpty()) {
            int c = queue.poll();
            seen++;
            for (int nxt : graph.get(c)) {
                indegree.put(nxt, indegree.get(nxt) - 1);
                if (indegree.get(nxt) == 0) {
                    queue.add(nxt);
                }
            }
        }
        return seen == colors.size();
    }
}
