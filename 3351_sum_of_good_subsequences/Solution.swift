// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

class Solution {
    func sumOfGoodSubsequences(_ nums: [Int]) -> Int {
        let mod = 1_000_000_007
        var cnt = [Int: Int]()
        var sum = [Int: Int]()
        var ans = 0
        for x in nums {
            var c = 1
            var s = x
            if cnt[x - 1, default: 0] > 0 {
                c = (c + cnt[x - 1]!) % mod
                s = (s + sum[x - 1]! + cnt[x - 1]! * x % mod) % mod
            }
            if cnt[x + 1, default: 0] > 0 {
                c = (c + cnt[x + 1]!) % mod
                s = (s + sum[x + 1]! + cnt[x + 1]! * x % mod) % mod
            }
            cnt[x, default: 0] = (cnt[x, default: 0] + c) % mod
            sum[x, default: 0] = (sum[x, default: 0] + s) % mod
            ans = (ans + s) % mod
        }
        return ans
    }
}
