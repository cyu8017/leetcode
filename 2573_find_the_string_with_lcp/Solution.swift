// LeetCode 2573 - Find the String with LCP
// https://leetcode.com/problems/find-the-string-with-lcp/

class Solution {
    func findTheString(_ lcp: [[Int]]) -> String {
        let n = lcp.count
        var s = [Character](repeating: Character(UnicodeScalar(0)), count: n)
        var c = Character("a")
        for i in 0..<n {
            if s[i] != Character(UnicodeScalar(0)) { continue }
            if c > "z" { return "" }
            s[i] = c
            if i + 1 < n {
                for j in (i + 1)..<n where lcp[i][j] > 0 { s[j] = c }
            }
            c = Character(UnicodeScalar(c.asciiValue! + 1))
        }
        for i in stride(from: n - 1, through: 0, by: -1) {
            for j in stride(from: n - 1, through: 0, by: -1) {
                var v = 0
                if s[i] == s[j] {
                    v = 1
                    if i + 1 < n && j + 1 < n { v += lcp[i + 1][j + 1] }
                }
                if lcp[i][j] != v { return "" }
            }
        }
        return String(s)
    }
}
