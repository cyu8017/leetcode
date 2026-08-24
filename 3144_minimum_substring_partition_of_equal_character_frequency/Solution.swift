// LeetCode 3144 - Minimum Substring Partition of Equal Character Frequency
// https://leetcode.com/problems/minimum-substring-partition-of-equal-character-frequency/

class Solution {
    private var chars: [Character] = []
    private var n = 0
    private var memo: [Int] = []

    func minimumSubstringsInPartition(_ s: String) -> Int {
        chars = Array(s)
        n = chars.count
        memo = Array(repeating: -1, count: n)
        return dfs(0)
    }

    private func dfs(_ i: Int) -> Int {
        if i >= n { return 0 }
        if memo[i] != -1 { return memo[i] }
        var cnt = Array(repeating: 0, count: 26)
        var freq: [Int: Int] = [:]
        memo[i] = n - i
        let a = Character("a").asciiValue!
        for j in i..<n {
            let k = Int(chars[j].asciiValue! - a)
            if cnt[k] > 0 {
                let c = cnt[k]
                freq[c]! -= 1
                if freq[c] == 0 { freq.removeValue(forKey: c) }
            }
            cnt[k] += 1
            freq[cnt[k], default: 0] += 1
            if freq.count == 1 {
                memo[i] = min(memo[i], 1 + dfs(j + 1))
            }
        }
        return memo[i]
    }
}
