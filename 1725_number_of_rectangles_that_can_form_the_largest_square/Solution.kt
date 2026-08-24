// LeetCode 1725 - Number Of Rectangles That Can Form The Largest Square
// https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution {
    fun countGoodRectangles(rectangles: Array<IntArray>): Int {
        var best = 0
        var count = 0
        for (rect in rectangles) {
            val side = minOf(rect[0], rect[1])
            if (side > best) {
                best = side
                count = 1
            } else if (side == best) {
                count++
            }
        }
        return count
    }
}
