// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int SmallestCommonElement(int[][] mat) {
        var common = new HashSet<int>(mat[0]);
        for (int i = 1; i < mat.Length; i++) {
            common.IntersectWith(mat[i]);
            if (common.Count == 0) return -1;
        }
        return common.Min();
    }
}
