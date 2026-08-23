// LeetCode 3242 - Design Neighbor Sum Service
// https://leetcode.com/problems/design-neighbor-sum-service/

import java.util.HashMap;
import java.util.Map;

class NeighborSum {
    private final int[][] grid;
    private final Map<Integer, int[]> d = new HashMap<>();
    private final int[][] dirs = {
        {-1, 0, 1, 0, -1},
        {-1, 1, 1, -1, -1}
    };

    public NeighborSum(int[][] grid) {
        this.grid = grid;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                d.put(grid[i][j], new int[] {i, j});
            }
        }
    }

    private int cal(int value, int k) {
        int[] p = d.get(value);
        int s = 0;
        for (int q = 0; q < 4; q++) {
            int x = p[0] + dirs[k][q], y = p[1] + dirs[k][q + 1];
            if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length) {
                s += grid[x][y];
            }
        }
        return s;
    }

    public int adjacentSum(int value) {
        return cal(value, 0);
    }

    public int diagonalSum(int value) {
        return cal(value, 1);
    }
}
