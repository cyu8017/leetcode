// LeetCode 1725 - Number Of Rectangles That Can Form The Largest Square
// https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

public class Solution {
    public int CountGoodRectangles(int[][] rectangles) {
        int best = 0;
        int count = 0;
        foreach (int[] rect in rectangles) {
            int side = System.Math.Min(rect[0], rect[1]);
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
