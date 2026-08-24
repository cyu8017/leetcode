// LeetCode 3250 - Find the Count of Monotonic Pairs I
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/

class Solution {
    func countOfPairs(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        let n = nums.count
        var dp = Array(repeating: 0, count: 51)
        for a in 0...nums[0] { dp[a] = 1 }
        if n >= 2 {
            for i in 1..<n {
                var ndp = Array(repeating: 0, count: 51)
                var pref = Array(repeating: 0, count: 52)
                for a in 0...50 { pref[a + 1] = (pref[a] + dp[a]) % mod }
                for a2 in 0...nums[i] {
                    let b2 = nums[i] - a2
                    var maxA1 = a2
                    let lim = nums[i - 1] - b2
                    if lim < maxA1 { maxA1 = lim }
                    if maxA1 < 0 { continue }
                    if maxA1 > 50 { maxA1 = 50 }
                    ndp[a2] = pref[maxA1 + 1]
                }
                dp = ndp
            }
        }
        return dp.reduce(0) { ($0 + $1) % mod }
    }
}
