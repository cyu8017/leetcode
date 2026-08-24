// LeetCode 3031 - Minimum Time to Revert Word to Initial State II
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/

class Solution {
    func minimumTimeToInitialState(_ word: String, _ k: Int) -> Int {
        let hashing = Hashing(word, 13331, 998244353)
        let n = word.count
        var i = k
        while i < n {
            if hashing.query(1, n - i) == hashing.query(i + 1, n) { return i / k }
            i += k
        }
        return (n + k - 1) / k
    }
}

private class Hashing {
    private var p: [Int]
    private var h: [Int]
    private let mod: Int

    init(_ word: String, _ bas: Int, _ mod: Int) {
        self.mod = mod
        let n = word.count
        p = Array(repeating: 0, count: n + 1)
        h = Array(repeating: 0, count: n + 1)
        p[0] = 1
        let chars = Array(word)
        let aVal = Int(Character("a").asciiValue!)
        for i in 1...n {
            p[i] = p[i - 1] * bas % mod
            h[i] = (h[i - 1] * bas + (Int(chars[i - 1].asciiValue!) - aVal)) % mod
        }
    }

    func query(_ l: Int, _ r: Int) -> Int {
        return (h[r] - h[l - 1] * p[r - l + 1] % mod + mod) % mod
    }
}
