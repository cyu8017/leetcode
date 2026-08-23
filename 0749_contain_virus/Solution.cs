// LeetCode 0749 - Contain Virus
// https://leetcode.com/problems/contain-virus/

using System.Collections.Generic;

public class Solution {
    public int ContainVirus(int[][] isInfected) {
        int m = isInfected.Length, n = isInfected[0].Length, walls = 0;
        while (true) {
            var seen = new HashSet<(int, int)>();
            var regions = new List<HashSet<(int, int)>>();
            var frontiers = new List<HashSet<(int, int)>>();
            var perimeters = new List<int>();
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (isInfected[i][j] == 1 && !seen.Contains((i, j))) {
                        var stack = new List<(int, int)> { (i, j) };
                        seen.Add((i, j));
                        var region = new HashSet<(int, int)>();
                        var frontier = new HashSet<(int, int)>();
                        int perimeter = 0;
                        int[][] dirs = { new[] { -1, 0 }, new[] { 1, 0 }, new[] { 0, -1 }, new[] { 0, 1 } };
                        while (stack.Count > 0) {
                            var (r, c) = stack[stack.Count - 1];
                            stack.RemoveAt(stack.Count - 1);
                            region.Add((r, c));
                            foreach (var d in dirs) {
                                int nr = r + d[0], nc = c + d[1];
                                if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                                if (isInfected[nr][nc] == 1 && seen.Add((nr, nc))) stack.Add((nr, nc));
                                else if (isInfected[nr][nc] == 0) { frontier.Add((nr, nc)); perimeter++; }
                            }
                        }
                        regions.Add(region);
                        frontiers.Add(frontier);
                        perimeters.Add(perimeter);
                    }
                }
            }
            if (regions.Count == 0) break;
            int quarantine = 0;
            for (int i = 1; i < regions.Count; i++)
                if (frontiers[i].Count > frontiers[quarantine].Count) quarantine = i;
            if (frontiers[quarantine].Count == 0) break;
            walls += perimeters[quarantine];
            foreach (var (r, c) in regions[quarantine]) isInfected[r][c] = -1;
            for (int index = 0; index < frontiers.Count; index++) {
                if (index == quarantine) continue;
                foreach (var (r, c) in frontiers[index]) isInfected[r][c] = 1;
            }
        }
        return walls;
    }
}
