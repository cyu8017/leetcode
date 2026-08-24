// LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

class Solution {
    private var ans = 0
    private var freq: [Int: Int] = [:]
    private var g: [[Int]] = []
    private var s: [Character] = []

    func countPalindromePaths(_ parent: [Int], _ s: String) -> Int {
        let n = parent.count
        self.s = Array(s)
        g = Array(repeating: [], count: n)
        for i in 1..<n { g[parent[i]].append(i) }
        freq = [0: 1]
        ans = 0
        dfs(0, 0)
        return ans
    }

    private func dfs(_ u: Int, _ mask: Int) {
        for v in g[u] {
            let nm = mask ^ (1 << Int(s[v].asciiValue! - 97))
            ans += freq[nm, default: 0]
            for b in 0..<26 { ans += freq[nm ^ (1 << b), default: 0] }
            freq[nm, default: 0] += 1
            dfs(v, nm)
        }
    }
}
