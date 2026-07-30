// LeetCode 1380 - Lucky Numbers In A Matrix
// https://leetcode.com/problems/lucky-numbers-in-a-matrix/

using System.Collections.Generic;
using System.Linq;
public class Solution {
    public IList<int> LuckyNumbers(int[][] matrix) {
        var mins = new HashSet<int>(matrix.Select(r => r.Min()));
        var maxs = new HashSet<int>();
        for (int c = 0; c < matrix[0].Length; c++) {
            int mx = int.MinValue;
            for (int r = 0; r < matrix.Length; r++) mx = System.Math.Max(mx, matrix[r][c]);
            maxs.Add(mx);
        }
        mins.IntersectWith(maxs);
        return mins.ToList();
    }
}
