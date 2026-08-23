// LeetCode 3417 - Zigzag Grid Traversal With Skip
// https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] zigzagTraversal(int[][] grid) {
        List<Integer> ans = new ArrayList<>();
        boolean skip = false;
        for (int i = 0; i < grid.length; i++) {
            int[] row = grid[i];
            if (i % 2 == 0) {
                for (int v : row) {
                    if (!skip) ans.add(v);
                    skip = !skip;
                }
            } else {
                for (int j = row.length - 1; j >= 0; j--) {
                    if (!skip) ans.add(row[j]);
                    skip = !skip;
                }
            }
        }
        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) res[i] = ans.get(i);
        return res;
    }
}
