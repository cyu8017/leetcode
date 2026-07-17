// LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int[] getBiggestThree(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int[][] s1 = new int[m + 2][n + 2];
        int[][] s2 = new int[m + 2][n + 2];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int value = grid[i][j];
                s1[i + 1][j + 1] = s1[i][j] + value;
                s2[i + 1][j + 1] = s2[i][j + 2] + value;
            }
        }

        Set<Integer> rhombusSums = new HashSet<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int pi = i + 1;
                int pj = j + 1;
                int value = grid[i][j];
                int limit = Math.min(Math.min(i, m - 1 - i), Math.min(j, n - 1 - j));
                rhombusSums.add(value);
                for (int k = 1; k <= limit; k++) {
                    int a = s1[pi + k][pj] - s1[pi][pj - k];
                    int b = s1[pi][pj + k] - s1[pi - k][pj];
                    int c = s2[pi][pj - k] - s2[pi - k][pj];
                    int d = s2[pi + k][pj] - s2[pi][pj + k];
                    rhombusSums.add(
                            a + b + c + d - grid[i + k][j] + grid[i - k][j]
                    );
                }
            }
        }

        List<Integer> sorted = new ArrayList<>(rhombusSums);
        sorted.sort(Collections.reverseOrder());
        int size = Math.min(3, sorted.size());
        int[] result = new int[size];
        for (int i = 0; i < size; i++) {
            result[i] = sorted.get(i);
        }
        return result;
    }
}
