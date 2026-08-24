// LeetCode 2484 - Count Palindromic Subsequences
// https://leetcode.com/problems/count-palindromic-subsequences/

class Solution {
    func countPalindromes(_ s: String) -> Int {
        let mod = 1_000_000_007
        let chars = Array(s)
        let n = chars.count
        var pref = [[[Int]]](repeating: [[Int]](repeating: [Int](repeating: 0, count: 10), count: 10), count: n)
        var suf = [[[Int]]](repeating: [[Int]](repeating: [Int](repeating: 0, count: 10), count: 10), count: n)
        var cnt = [Int](repeating: 0, count: 10)
        for i in 0..<n {
            if i > 0 {
                for a in 0..<10 { pref[i][a] = pref[i - 1][a] }
            }
            let d = Int(chars[i].asciiValue! - Character("0").asciiValue!)
            for a in 0..<10 { pref[i][a][d] += cnt[a] }
            cnt[d] += 1
        }
        cnt = [Int](repeating: 0, count: 10)
        for i in stride(from: n - 1, through: 0, by: -1) {
            if i + 1 < n {
                for a in 0..<10 { suf[i][a] = suf[i + 1][a] }
            }
            let d = Int(chars[i].asciiValue! - Character("0").asciiValue!)
            for a in 0..<10 { suf[i][a][d] += cnt[a] }
            cnt[d] += 1
        }
        var ans = 0
        if n > 4 {
            for i in 2..<(n - 2) {
                for a in 0..<10 {
                    for b in 0..<10 {
                        ans = (ans + pref[i - 1][a][b] * suf[i + 1][a][b]) % mod
                    }
                }
            }
        }
        return ans
    }
}
