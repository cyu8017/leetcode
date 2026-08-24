// LeetCode 2748 - Number of Beautiful Pairs
// https://leetcode.com/problems/number-of-beautiful-pairs/

class Solution {
    func countBeautifulPairs(_ nums: [Int]) -> Int {
        var ans = 0
        var freq = Array(repeating: 0, count: 10)
        for x in nums {
            let last = x % 10
            for d in 1...9 where freq[d] > 0 && gcd(d, last) == 1 {
                ans += freq[d]
            }
            freq[firstDigit(x)] += 1
        }
        return ans
    }

    private func firstDigit(_ x: Int) -> Int {
        var v = x
        while v >= 10 { v /= 10 }
        return v
    }

    private func gcd(_ a: Int, _ b: Int) -> Int {
        var x = a, y = b
        while y != 0 { let t = x % y; x = y; y = t }
        return x
    }
}
