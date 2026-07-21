// LeetCode 1812 - Determine Color of a Chessboard Square
// https://leetcode.com/problems/determine-color-of-a-chessboard-square/

public class Solution {
    public bool SquareIsWhite(string coordinates) {
        int col = coordinates[0] - 'a' + 1;
        int row = coordinates[1] - '0';
        return (col + row) % 2 == 1;
    }
}
