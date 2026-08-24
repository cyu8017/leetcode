// LeetCode 3146 - Permutation Difference between Two Strings
// https://leetcode.com/problems/permutation-difference-between-two-strings/

class Solution {
    func findPermutationDifference(_ s: String, _ t: String) -> Int {
        var d = Array(repeating: 0, count: 26)
        let a = Character("a").asciiValue!
        let sc = Array(s), tc = Array(t)
        for i in 0..<sc.count { d[Int(sc[i].asciiValue! - a)] = i }
        var ans = 0
        for i in 0..<tc.count { ans += abs(d[Int(tc[i].asciiValue! - a)] - i) }
        return ans
    }
}
