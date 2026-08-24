// LeetCode 2183 - Count Array Pairs Divisible by K
// https://leetcode.com/problems/count-array-pairs-divisible-by-k/

class Solution {
    func countPairs(_ nums: [Int], _ k: Int) -> Int {
        func gcd(_ a: Int, _ b: Int) -> Int {
            var a = a, b = b
            while b != 0 { let t = a % b; a = b; b = t }
            return a
        }
        var freq = [Int: Int]()
        var ans = 0
        for x in nums {
            let g1 = gcd(x, k)
            for (g, c) in freq where g1 * g % k == 0 { ans += c }
            freq[g1, default: 0] += 1
        }
        return ans
    }
}
