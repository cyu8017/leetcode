// LeetCode 3242 - Design Neighbor Sum Service
// https://leetcode.com/problems/design-neighbor-sum-service/

using System.Collections.Generic;

public class NeighborSum {
    int[][] grid;
    Dictionary<int, (int, int)> d = new Dictionary<int, (int, int)>();
    int[][] dirs = new int[][] {
        new int[] { -1, 0, 1, 0, -1 },
        new int[] { -1, 1, 1, -1, -1 }
    };

    public NeighborSum(int[][] grid) {
        this.grid = grid;
        for (int i = 0; i < grid.Length; i++) {
            for (int j = 0; j < grid[i].Length; j++) {
                d[grid[i][j]] = (i, j);
            }
        }
    }

    int Cal(int value, int k) {
        var p = d[value];
        int s = 0;
        for (int q = 0; q < 4; q++) {
            int x = p.Item1 + dirs[k][q], y = p.Item2 + dirs[k][q + 1];
            if (x >= 0 && x < grid.Length && y >= 0 && y < grid[0].Length) {
                s += grid[x][y];
            }
        }
        return s;
    }

    public int AdjacentSum(int value) => Cal(value, 0);
    public int DiagonalSum(int value) => Cal(value, 1);
}
