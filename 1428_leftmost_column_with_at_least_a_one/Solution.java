// LeetCode 1428 - Leftmost Column With At Least A One
// https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

import java.util.*;

class BinaryMatrix {
    public int get(int row, int col) { throw new UnsupportedOperationException(); }
    public List<Integer> dimensions() { throw new UnsupportedOperationException(); }
}

class Solution {
    public int leftMostColumnWithOne(BinaryMatrix binaryMatrix) {
        List<Integer> dim = binaryMatrix.dimensions();
        int rows = dim.get(0), cols = dim.get(1), row = 0, col = cols - 1, answer = -1;
        while (row < rows && col >= 0) {
            if (binaryMatrix.get(row, col) == 1) { answer = col; col--; }
            else row++;
        }
        return answer;
    }
}
