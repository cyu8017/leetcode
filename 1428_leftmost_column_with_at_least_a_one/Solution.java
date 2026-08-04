// LeetCode 1428 - Leftmost Column With At Least A One
// https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

import java.util.*;

class BinaryMatrix {
    public int get(int row, int col) { throw new System.NotImplementedException(); }
    public List<Integer> dimensions() { throw new System.NotImplementedException(); }
}
class Solution {
    public int leftMostColumnWithOne(BinaryMatrix binaryMatrix) {
        var dim = binaryMatrix.Dimensions();
        int rows = dim[0], cols = dim[1], row = 0, col = cols - 1, answer = -1;
        while (row < rows && col >= 0) {
            if (binaryMatrix.Get(row, col) == 1) { answer = col; col--; }
            else row++;
        }
        return answer;
    }
}
