// LeetCode 3274 - Check if Two Chessboard Squares Have the Same Color
// https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/

class Solution {
    public boolean checkTwoChessboards(String coordinate1, String coordinate2) {
        int c1 = (coordinate1.charAt(0) - 'a') + (coordinate1.charAt(1) - '1');
        int c2 = (coordinate2.charAt(0) - 'a') + (coordinate2.charAt(1) - '1');
        return c1 % 2 == c2 % 2;
    }
}
