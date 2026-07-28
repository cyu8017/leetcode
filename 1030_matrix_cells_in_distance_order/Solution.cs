// LeetCode 1030 - Matrix Cells in Distance Order
// https://leetcode.com/problems/matrix-cells-in-distance-order/

using System;
using System.Linq;

public class Solution {
    public int[][] AllCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        var cells = new int[rows * cols][];
        int idx = 0;
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                cells[idx++] = new[] { r, c };
        Array.Sort(cells, (a, b) =>
            (Math.Abs(a[0] - rCenter) + Math.Abs(a[1] - cCenter))
                .CompareTo(Math.Abs(b[0] - rCenter) + Math.Abs(b[1] - cCenter)));
        return cells;
    }
}
