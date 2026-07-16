// LeetCode 0118 - Pascal's Triangle
// https://leetcode.com/problems/pascals-triangle/

using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> Generate(int numRows) {
        var triangle = new List<IList<int>>();
        for (int row = 0; row < numRows; row++) {
            var values = new List<int>();
            for (int col = 0; col <= row; col++) {
                values.Add(col == 0 || col == row ? 1 :
                    triangle[row - 1][col - 1] + triangle[row - 1][col]);
            }
            triangle.Add(values);
        }
        return triangle;
    }
}