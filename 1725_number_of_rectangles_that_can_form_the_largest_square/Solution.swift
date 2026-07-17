// LeetCode 1725 - Number Of Rectangles That Can Form The Largest Square
// https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution {
    func countGoodRectangles(_ rectangles: [[Int]]) -> Int {
        var best = 0
        var count = 0
        for rect in rectangles {
            let side = min(rect[0], rect[1])
            if side > best {
                best = side
                count = 1
            } else if side == best {
                count += 1
            }
        }
        return count
    }
}
