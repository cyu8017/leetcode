// LeetCode 1725 - Number Of Rectangles That Can Form The Largest Square
// https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution {
    public int countGoodRectangles(int[][] rectangles) {
        int best = 0;
        int count = 0;
        for (int[] rect : rectangles) {
            int side = Math.min(rect[0], rect[1]);
            if (side > best) {
                best = side;
                count = 1;
            } else if (side == best) {
                count++;
            }
        }
        return count;
    }
}
