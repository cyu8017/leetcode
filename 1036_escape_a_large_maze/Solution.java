// LeetCode 1036 - Escape a Large Maze
// https://leetcode.com/problems/escape-a-large-maze/

import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

class Solution {
    // Harness emits empty int[][] as new int[0]; overload accepts that form.
    public boolean isEscapePossible(int[] blocked, int[] source, int[] target) {
        return isEscapePossible(new int[0][], source, target);
    }

    public boolean isEscapePossible(int[][] blocked, int[] source, int[] target) {
        Set<Long> blockedSet = new HashSet<>();
        for (int[] b : blocked) blockedSet.add(key(b[0], b[1]));
        int limit = blocked.length * (blocked.length - 1) / 2;
        return bfs(source, target, blockedSet, limit) && bfs(target, source, blockedSet, limit);
    }

    private boolean bfs(int[] start, int[] goal, Set<Long> blockedSet, int limit) {
        Queue<long[]> q = new ArrayDeque<>();
        Set<Long> seen = new HashSet<>();
        q.offer(new long[]{start[0], start[1]});
        seen.add(key(start[0], start[1]));
        int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        while (!q.isEmpty()) {
            if (seen.size() > limit) return true;
            long[] cur = q.poll();
            int r = (int) cur[0], c = (int) cur[1];
            if (r == goal[0] && c == goal[1]) return true;
            for (int[] d : dirs) {
                int nr = r + d[0], nc = c + d[1];
                long k = key(nr, nc);
                if (nr >= 0 && nr < 1_000_000 && nc >= 0 && nc < 1_000_000
                        && !blockedSet.contains(k) && seen.add(k)) {
                    q.offer(new long[]{nr, nc});
                }
            }
        }
        return false;
    }

    private long key(int r, int c) {
        return (((long) r) << 32) | (c & 0xffffffffL);
    }
}
