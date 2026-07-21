// LeetCode 1874 - Minimize Product Sum of Two Arrays
// https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

class Solution {
    func minProductSum(_ nums1: [Int], _ nums2: [Int]) -> Int {
        let a = nums1.sorted()
        let b = nums2.sorted(by: >)
        var total = 0
        for i in 0..<a.count {
            total += a[i] * b[i]
        }
        return total
    }
}
