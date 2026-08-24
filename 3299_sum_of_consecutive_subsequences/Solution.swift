// LeetCode 3299 - Sum of Consecutive Subsequences
// https://leetcode.com/problems/sum-of-consecutive-subsequences/

class Solution {
    func rangeSum(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        var cnt = [Int: Int]()
        var sum = [Int: Int]()
        var ans = 0
        for x in nums {
            let cL = cnt[x - 1, default: 0], sL = sum[x - 1, default: 0]
            let cR = cnt[x + 1, default: 0], sR = sum[x + 1, default: 0]
            var c = (1 + cL + cR) % mod
            var s = (x + sL + cL * x % mod + sR + cR * x % mod) % mod
            if cL > 0 && cR > 0 {
                c = (c + cL * cR % mod) % mod
                s = (s + sL * cR % mod + sR * cL % mod + cL * cR % mod * x % mod) % mod
            }
            cnt[x, default: 0] = (cnt[x, default: 0] + c) % mod
            sum[x, default: 0] = (sum[x, default: 0] + s) % mod
            ans = (ans + s) % mod
        }
        return ans
    }
}
