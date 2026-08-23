// LeetCode 2732 - Find a Good Subset of the Matrix
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public List<Integer> goodSubsetofBinaryMatrix(int[][] grid) {
        int n = grid[0].length;
        Map<Integer, Integer> first = new HashMap<>();
        for (int i = 0; i < grid.length; i++) {
            int mask = 0;
            for (int j = 0; j < n; j++) if (grid[i][j] == 1) mask |= 1 << j;
            if (mask == 0) return List.of(i);
            for (Map.Entry<Integer, Integer> kv : first.entrySet()) {
                if ((kv.getKey() & mask) == 0) {
                    int a = kv.getValue(), b = i;
                    if (a < b) return Arrays.asList(a, b);
                    return Arrays.asList(b, a);
                }
            }
            first.putIfAbsent(mask, i);
        }
        return new ArrayList<>();
    }
}
