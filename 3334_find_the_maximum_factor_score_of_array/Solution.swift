// LeetCode 3334 - Find the Maximum Factor Score of Array
// https://leetcode.com/problems/find-the-maximum-factor-score-of-array/

class Solution {
    func maxScore(_ nums: [Int]) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        func lcm(_ a: Int, _ b: Int) -> Int {
            if a == 0 || b == 0 { return 0 }
            return a / gcd(a, b) * b
        }
        let n = nums.count
        var gcdAll = nums[0], lcmAll = nums[0]
        for i in 1..<n {
            gcdAll = gcd(gcdAll, nums[i])
            lcmAll = lcm(lcmAll, nums[i])
        }
        var ans = gcdAll * lcmAll
        for skip in 0..<n {
            var g = 0, l = 1
            var first = true
            for i in 0..<n where i != skip {
                if first { g = nums[i]; l = nums[i]; first = false }
                else { g = gcd(g, nums[i]); l = lcm(l, nums[i]) }
            }
            if first { continue }
            let v = g * l
            if v > ans { ans = v }
        }
        return ans
    }
}
