// LeetCode 0152 - Maximum Product Subarray
// https://leetcode.com/problems/maximum-product-subarray/

class Solution {
    func maxProduct(_ nums: [Int]) -> Int {
        var best = nums[0]
        var maxProduct = nums[0]
        var minProduct = nums[0]
        for number in nums.dropFirst() {
            let candidates = [number, maxProduct * number, minProduct * number]
            maxProduct = candidates.max()!
            minProduct = candidates.min()!
            best = max(best, maxProduct)
        }
        return best
    }
}