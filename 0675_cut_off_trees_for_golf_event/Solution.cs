// LeetCode 0675 - Cut Off Trees for Golf Event
// https://leetcode.com/problems/cut-off-trees-for-golf-event/

using System;
using System.Collections.Generic;

public class Solution {
    public int CutOffTree(IList<IList<int>> forest) {
        var trees = new List<(int height, int r, int c)>();
        for (int i = 0; i < forest.Count; ++i) {
            for (int j = 0; j < forest[0].Count; ++j) {
                if (forest[i][j] > 1) trees.Add((forest[i][j], i, j));
            }
        }
        trees.Sort();
        int sr = 0, sc = 0, steps = 0;
        foreach (var (_, tr, tc) in trees) {
            int dist = Bfs(forest, sr, sc, tr, tc);
            if (dist < 0) return -1;
            steps += dist;
            sr = tr;
            sc = tc;
        }
        return steps;
    }

    private int Bfs(IList<IList<int>> forest, int sr, int sc, int tr, int tc) {
        if (sr == tr && sc == tc) return 0;
        int m = forest.Count, n = forest[0].Count;
        bool[,] seen = new bool[m, n];
        var queue = new Queue<(int r, int c, int dist)>();
        queue.Enqueue((sr, sc, 0));
        seen[sr, sc] = true;
        int[][] dirs = { new[]{-1,0}, new[]{1,0}, new[]{0,-1}, new[]{0,1} };
        while (queue.Count > 0) {
            var (r, c, dist) = queue.Dequeue();
            foreach (var dir in dirs) {
                int nr = r + dir[0], nc = c + dir[1];
                if (nr < 0 || nr >= m || nc < 0 || nc >= n || seen[nr, nc] || forest[nr][nc] == 0) continue;
                if (nr == tr && nc == tc) return dist + 1;
                seen[nr, nc] = true;
                queue.Enqueue((nr, nc, dist + 1));
            }
        }
        return -1;
    }
}
