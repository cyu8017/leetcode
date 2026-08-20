// LeetCode 1255 - Maximum Score Words Formed by Letters
// https://leetcode.com/problems/maximum-score-words-formed-by-letters/

class Solution {
    func maxScoreWords(_ words: [String], _ letters: [Character], _ score: [Int]) -> Int {
        var available = [Int](repeating: 0, count: 26)
        for ch in letters { available[Int(ch.asciiValue! - 97)] += 1 }
        let n = words.count
        var counts = [[Int]](repeating: [Int](repeating: 0, count: 26), count: n)
        for i in 0..<n {
            for ch in words[i] { counts[i][Int(ch.asciiValue! - 97)] += 1 }
        }
        var ans = 0
        func dfs(_ i: Int, _ rem: [Int], _ cur: Int) {
            ans = max(ans, cur)
            if i == n { return }
            dfs(i + 1, rem, cur)
            var next = rem
            var add = 0
            var ok = true
            for c in 0..<26 {
                if counts[i][c] > next[c] { ok = false; break }
                next[c] -= counts[i][c]
                add += counts[i][c] * score[c]
            }
            if ok { dfs(i + 1, next, cur + add) }
        }
        dfs(0, available, 0)
        return ans
    }
}
