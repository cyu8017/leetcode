// LeetCode 1424 - Diagonal Traverse Ii
// https://leetcode.com/problems/diagonal-traverse-ii/

import java.util.*;

class Solution {
    public int[] findDiagonalOrder(List<List<Integer>> nums) {
        Map<Integer, List<Integer>> diagonals = new TreeMap<>();
        for (int row = 0; row < nums.size(); row++) {
            List<Integer> values = nums.get(row);
            for (int col = 0; col < values.size(); col++) {
                diagonals.computeIfAbsent(row + col, k -> new ArrayList<>()).add(values.get(col));
            }
        }
        List<Integer> out = new ArrayList<>();
        for (List<Integer> diag : diagonals.values()) {
            for (int i = diag.size() - 1; i >= 0; i--) out.add(diag.get(i));
        }
        int[] ans = new int[out.size()];
        for (int i = 0; i < out.size(); i++) ans[i] = out.get(i);
        return ans;
    }
}
