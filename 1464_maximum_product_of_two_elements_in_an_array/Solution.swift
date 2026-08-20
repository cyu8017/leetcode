// LeetCode 1464 - Maximum Product of Two Elements in an Array
// https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution {
    func maxProduct(_ nums: [Int]) -> Int {
        let sorted = nums.sorted()
        let a = sorted[sorted.count - 2], b = sorted[sorted.count - 1]
        return (a - 1) * (b - 1)
    }
}
