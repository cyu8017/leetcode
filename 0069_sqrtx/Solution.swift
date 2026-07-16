// LeetCode 0069 - Sqrt(x)
// https://leetcode.com/problems/sqrtx/

class Solution {
    func mySqrt(_ x: Int) -> Int {
        if x < 2 {
            return x
        }

        var left = 2
        var right = x / 2

        while left <= right {
            let mid = left + (right - left) / 2
            let square = mid * mid
            if square == x {
                return mid
            }
            if square < x {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }

        return right
    }
}
