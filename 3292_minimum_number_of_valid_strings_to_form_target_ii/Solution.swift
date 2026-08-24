// LeetCode 3292 - Minimum Number of Valid Strings to Form Target II
// https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/

class Solution {
    func minValidStrings(_ words: [String], _ target: String) -> Int {
        let t = Array(target)
        let n = t.count
        let inf = 1_000_000_000
        var dp = Array(repeating: inf, count: n + 1)
        dp[0] = 0
        let root = TrieNode()
        for w in words {
            var cur = root
            for c in w {
                let ci = Int(c.asciiValue! - 97)
                if cur.next[ci] == nil { cur.next[ci] = TrieNode() }
                cur = cur.next[ci]!
            }
        }
        for i in 0..<n {
            if dp[i] == inf { continue }
            var cur: TrieNode? = root
            for j in i..<n {
                let ci = Int(t[j].asciiValue! - 97)
                guard let node = cur?.next[ci] else { break }
                cur = node
                if dp[i] + 1 < dp[j + 1] { dp[j + 1] = dp[i] + 1 }
            }
        }
        return dp[n] == inf ? -1 : dp[n]
    }
}

private class TrieNode {
    var next: [TrieNode?] = Array(repeating: nil, count: 26)
}
