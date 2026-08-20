// LeetCode 1987 - Number of Unique Good Subsequences
// https://leetcode.com/problems/number-of-unique-good-subsequences/

class Solution {
    func numberOfUniqueGoodSubsequences(_ binary: String) -> Int {
        let MOD = 1_000_000_007
        var ends0 = 0, ends1 = 0
        var has0 = false
        for ch in binary {
            if ch == "0" {
                has0 = true
                ends0 = (ends0 + ends1) % MOD
            } else {
                ends1 = (ends0 + ends1 + 1) % MOD
            }
        }
        return (ends0 + ends1 + (has0 ? 1 : 0)) % MOD
    }
}
