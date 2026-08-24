// LeetCode 4010 - Maximize Pair Strength Using GCD
// https://leetcode.com/problems/maximize-pair-strength-using-gcd/


class Solution {
    func maxPairStrength(_ nums: [Int]) -> Int {
        func gcd(_ a0: Int, _ b0: Int) -> Int {
            var a = a0, b = b0
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        let n = nums.count
        var ans = 0
        for i in 0..<n {
            for j in (i + 1)..<n {
                let g = gcd(nums[i], nums[j])
                let x = nums[i] * nums[j] / (g * g)
                ans = max(ans, x)
            }
        }
        return ans
    }
}
