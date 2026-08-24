// LeetCode 3579 - Minimum Steps to Convert String with Operations
// https://leetcode.com/problems/minimum-steps-to-convert-string-with-operations/

class Solution {
    var word1 = [Character]()
    var word2 = [Character]()

    func calc(_ l: Int, _ r: Int, _ rev: Bool) -> Int {
        var cnt = Array(repeating: Array(repeating: 0, count: 26), count: 26)
        var res = 0
        for i in l...r {
            let j = rev ? r - (i - l) : i
            let a = Int(word1[j].asciiValue! - 97)
            let b = Int(word2[i].asciiValue! - 97)
            if a != b {
                if cnt[b][a] > 0 { cnt[b][a] -= 1 }
                else { cnt[a][b] += 1; res += 1 }
            }
        }
        return res
    }

    func minOperations(_ word1: String, _ word2: String) -> Int {
        self.word1 = Array(word1)
        self.word2 = Array(word2)
        let n = self.word1.count
        var f = Array(repeating: Int.max / 2, count: n + 1)
        f[0] = 0
        for i in 1...n {
            for j in 0..<i {
                let a = calc(j, i - 1, false)
                let b = 1 + calc(j, i - 1, true)
                f[i] = min(f[i], f[j] + min(a, b))
            }
        }
        return f[n]
    }
}
