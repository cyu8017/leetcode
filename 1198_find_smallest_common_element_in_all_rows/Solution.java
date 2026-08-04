// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

import java.util.*;

class Solution {
    public int smallestCommonElement(int[][] mat) {
        Set<Integer> common = new HashSet<>();
        for (int x : mat[0]) common.add(x);
        for (int r = 1; r < mat.length; r++) {
            Set<Integer> row = new HashSet<>();
            for (int x : mat[r]) row.add(x);
            common.retainAll(row);
            if (common.isEmpty()) return -1;
        }
        int ans = Integer.MAX_VALUE;
        for (int x : common) ans = Math.min(ans, x);
        return ans;
    }
}
