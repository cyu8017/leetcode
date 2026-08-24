// LeetCode 2524 - Maximum Frequency Score of a Subarray
// https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

class Solution {
    func maxFrequencyScore(_ nums: [Int], _ k: Int) -> Int {
        let MOD = 1_000_000_007
        func modPow(_ a: Int, _ e: Int) -> Int {
            var a = ((a % MOD) + MOD) % MOD, e = e, res = 1
            while e > 0 {
                if e & 1 != 0 { res = res * a % MOD }
                a = a * a % MOD
                e >>= 1
            }
            return res
        }
        var freq = [Int: Int]()
        var score = 0, best = 0
        func add(_ x: Int) {
            let c = freq[x, default: 0]
            if c > 0 { score = (score - modPow(x, c) + MOD) % MOD }
            freq[x] = c + 1
            score = (score + modPow(x, c + 1)) % MOD
        }
        func remove(_ x: Int) {
            let c = freq[x]!
            score = (score - modPow(x, c) + MOD) % MOD
            if c == 1 { freq.removeValue(forKey: x) }
            else {
                freq[x] = c - 1
                score = (score + modPow(x, c - 1)) % MOD
            }
        }
        for i in 0..<nums.count {
            add(nums[i])
            if i >= k { remove(nums[i - k]) }
            if i >= k - 1 { best = max(best, score) }
        }
        return best
    }
}
