// LeetCode 3411 - Maximum Subarray With Equal Products
// https://leetcode.com/problems/maximum-subarray-with-equal-products/

class Solution {
    func maxLength(_ nums: [Int]) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        let n = nums.count
        var ans = 1
        for i in 0..<n {
            var prod = 1, g = 0, l = 1
            for j in i..<n {
                if prod > 1_000_000_000 / nums[j] { break }
                prod *= nums[j]
                if g == 0 { g = nums[j]; l = nums[j] }
                else {
                    g = gcd(g, nums[j])
                    l = l / gcd(l, nums[j]) * nums[j]
                }
                if prod == l * g && j - i + 1 > ans { ans = j - i + 1 }
            }
        }
        return ans
    }
}
