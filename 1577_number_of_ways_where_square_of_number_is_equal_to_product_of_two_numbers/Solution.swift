// LeetCode 1577 - Number of Ways Where Square of Number Is Equal to Product of Two Numbers
// https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

class Solution {
    func numTriplets(_ nums1: [Int], _ nums2: [Int]) -> Int {
        func count(_ a: [Int], _ b: [Int]) -> Int {
            var squares = [Int: Int]()
            for x in a { squares[x * x, default: 0] += 1 }
            var products = [Int: Int]()
            for i in 0..<b.count {
                for j in (i + 1)..<b.count {
                    products[b[i] * b[j], default: 0] += 1
                }
            }
            var ans = 0
            for (value, cnt) in squares {
                ans += cnt * (products[value] ?? 0)
            }
            return ans
        }
        return count(nums1, nums2) + count(nums2, nums1)
    }
}
