// LeetCode 0119 - Pascal's Triangle II
// https://leetcode.com/problems/pascals-triangle-ii/

using System.Collections.Generic;

public class Solution {
    public IList<int> GetRow(int rowIndex) {
        var row = new List<int>(new int[rowIndex + 1]);
        row[0] = 1;
        for (int i = 1; i <= rowIndex; i++) {
            for (int j = i; j >= 1; j--) row[j] += row[j - 1];
        }
        return row;
    }
}