// LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
// https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

class Solution {
    func minimumSplits(_ nums: [Int]) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 {
                let t = a % b
                a = b
                b = t
            }
            return a
        }
        var ans = 1
        var g = nums[0]
        for i in 1..<nums.count {
            let ng = gcd(g, nums[i])
            if ng == 1 {
                ans += 1
                g = nums[i]
            } else {
                g = ng
            }
        }
        return ans
    }
}
