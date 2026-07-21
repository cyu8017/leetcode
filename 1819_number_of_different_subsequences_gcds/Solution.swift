// LeetCode 1819 - Number of Different Subsequences GCDs
// https://leetcode.com/problems/number-of-different-subsequences-gcds/

class Solution {
    func countDifferentSubsequenceGCDs(_ nums: [Int]) -> Int {
        let maxVal = nums.max()!
        var present = Array(repeating: false, count: maxVal + 1)
        for num in nums { present[num] = true }

        func gcd(_ a: Int, _ b: Int) -> Int {
            var x = a, y = b
            while y != 0 {
                let t = x % y
                x = y
                y = t
            }
            return x
        }

        var ans = 0
        for g in 1...maxVal {
            var has = false
            var gcdVal = 0
            var multiple = g
            while multiple <= maxVal {
                if present[multiple] {
                    has = true
                    gcdVal = gcd(gcdVal, multiple / g)
                    if gcdVal == 1 { break }
                }
                multiple += g
            }
            if has && gcdVal == 1 { ans += 1 }
        }
        return ans
    }
}
