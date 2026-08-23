// LeetCode 0118 - Pascal's Triangle
// https://leetcode.com/problems/pascals-triangle/

import java.util.*;

class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>();
        for (int row = 0; row < numRows; row++) {
            List<Integer> values = new ArrayList<>();
            for (int col = 0; col <= row; col++) {
                if (col == 0 || col == row) values.add(1);
                else values.add(triangle.get(row - 1).get(col - 1)
                    + triangle.get(row - 1).get(col));
            }
            triangle.add(values);
        }
        return triangle;
    }
}