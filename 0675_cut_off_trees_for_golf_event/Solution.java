// LeetCode 0675 - Cut Off Trees for Golf Event
// https://leetcode.com/problems/cut-off-trees-for-golf-event/

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Queue;

class Solution {
    public int cutOffTree(List<List<Integer>> forest) {
        List<int[]> trees = new ArrayList<>();
        for (int i = 0; i < forest.size(); ++i) {
            for (int j = 0; j < forest.get(0).size(); ++j) {
                if (forest.get(i).get(j) > 1) {
                    trees.add(new int[] {forest.get(i).get(j), i, j});
                }
            }
        }
        Collections.sort(trees, (a, b) -> Integer.compare(a[0], b[0]));
        int sr = 0;
        int sc = 0;
        int steps = 0;
        for (int[] tree : trees) {
            int dist = bfs(forest, sr, sc, tree[1], tree[2]);
            if (dist < 0) {
                return -1;
            }
            steps += dist;
            sr = tree[1];
            sc = tree[2];
        }
        return steps;
    }

    private int bfs(List<List<Integer>> forest, int sr, int sc, int tr, int tc) {
        if (sr == tr && sc == tc) {
            return 0;
        }
        int m = forest.size();
        int n = forest.get(0).size();
        boolean[][] seen = new boolean[m][n];
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] {sr, sc, 0});
        seen[sr][sc] = true;
        int[][] dirs = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int r = cur[0];
            int c = cur[1];
            int dist = cur[2];
            for (int[] dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || seen[nr][nc] || forest.get(nr).get(nc) == 0) {
                    continue;
                }
                if (nr == tr && nc == tc) {
                    return dist + 1;
                }
                seen[nr][nc] = true;
                queue.offer(new int[] {nr, nc, dist + 1});
            }
        }
        return -1;
    }
}
