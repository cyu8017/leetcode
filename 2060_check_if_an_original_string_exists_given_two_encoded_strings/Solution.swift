// LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
// https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

class Solution {
    func possiblyEquals(_ s1: String, _ s2: String) -> Bool {
        let a = Array(s1), b = Array(s2)
        var memo = [String: Bool]()
        func isDigit(_ c: Character) -> Bool { c >= "0" && c <= "9" }
        func dfs(_ i: Int, _ j: Int, _ diff: Int) -> Bool {
            let key = "\(i),\(j),\(diff)"
            if let v = memo[key] { return v }
            let n = a.count, m = b.count
            if i == n && j == m {
                memo[key] = diff == 0
                return diff == 0
            }
            var res = false
            if diff == 0 && i < n && j < m && !isDigit(a[i]) && !isDigit(b[j]) {
                if a[i] == b[j] { res = dfs(i + 1, j + 1, 0) }
            } else if diff > 0 && i < n && !isDigit(a[i]) {
                res = dfs(i + 1, j, diff - 1)
            } else if diff < 0 && j < m && !isDigit(b[j]) {
                res = dfs(i, j + 1, diff + 1)
            }
            if !res && i < n && isDigit(a[i]) {
                var val = 0
                var p = i
                while p < n && isDigit(a[p]) {
                    val = val * 10 + Int(a[p].asciiValue! - 48)
                    if dfs(p + 1, j, diff + val) { res = true; break }
                    p += 1
                }
            }
            if !res && j < m && isDigit(b[j]) {
                var val = 0
                var p = j
                while p < m && isDigit(b[p]) {
                    val = val * 10 + Int(b[p].asciiValue! - 48)
                    if dfs(i, p + 1, diff - val) { res = true; break }
                    p += 1
                }
            }
            memo[key] = res
            return res
        }
        return dfs(0, 0, 0)
    }
}
