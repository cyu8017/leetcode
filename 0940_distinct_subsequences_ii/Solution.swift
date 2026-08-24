// LeetCode 0940 - Distinct Subsequences II
// https://leetcode.com/problems/distinct-subsequences-ii/

class Solution {
    func distinctSubseqII(_ s: String) -> Int {
        let mod = 1_000_000_007
        var ends = Array(repeating: 0, count: 26)
        var total = 1
        let a = Int(Character("a").asciiValue!)
        for ch in s {
            let i = Int(ch.asciiValue!) - a
            let prev = ends[i]
            ends[i] = total
            total = (total - prev + ends[i] + mod) % mod
        }
        return (total - 1 + mod) % mod
    }
}
