// LeetCode 3732 - Maximum Product of Three Elements After One Replacement
// https://leetcode.com/problems/maximum-product-of-three-elements-after-one-replacement/

class Solution {
    func maxProduct(_ nums: [Int]) -> Int {
        let a = nums.sorted()
        let n = a.count
        let x0 = a[0], x1 = a[1], x2 = a[n - 2], x3 = a[n - 1]
        let x = 100000
        return max(max(x0 * x1 * x, x2 * x3 * x), -x0 * x3 * x)
    }
}
