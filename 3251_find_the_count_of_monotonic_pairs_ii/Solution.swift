// LeetCode 3251 - Find the Count of Monotonic Pairs II
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

class Solution {
    func countOfPairs(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        let n = nums.count
        let maxV = nums.max()!
        var dp = Array(repeating: 0, count: maxV + 1)
        for a in 0...nums[0] { dp[a] = 1 }
        if n >= 2 {
            for i in 1..<n {
                var ndp = Array(repeating: 0, count: maxV + 1)
                var pref = Array(repeating: 0, count: maxV + 2)
                for a in 0...maxV { pref[a + 1] = (pref[a] + dp[a]) % mod }
                for a2 in 0...nums[i] {
                    let b2 = nums[i] - a2
                    var maxA1 = a2
                    let lim = nums[i - 1] - b2
                    if lim < maxA1 { maxA1 = lim }
                    if maxA1 < 0 { continue }
                    if maxA1 > maxV { maxA1 = maxV }
                    ndp[a2] = pref[maxA1 + 1]
                }
                dp = ndp
            }
        }
        return dp.reduce(0) { ($0 + $1) % mod }
    }
}
