// LeetCode 1913 - Maximum Product Difference Between Two Pairs
// https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

class Solution {
    func maxProductDifference(_ nums: [Int]) -> Int {
        var a = 0, b = 0
        var c = 100_000, d = 100_000
        for x in nums {
            if x > a {
                b = a; a = x
            } else if x > b {
                b = x
            }
            if x < c {
                d = c; c = x
            } else if x < d {
                d = x
            }
        }
        return a * b - c * d
    }
}
