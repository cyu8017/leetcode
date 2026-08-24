// LeetCode 3474 - Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/

class Solution {
    func generateString(_ str1: String, _ str2: String) -> String {
        let s1 = Array(str1), s2 = Array(str2)
        let n = s1.count, m = s2.count
        let L = n + m - 1
        var ans = Array(repeating: Character("?"), count: L)
        for i in 0..<n where s1[i] == "T" {
            for j in 0..<m {
                if ans[i + j] != "?" && ans[i + j] != s2[j] { return "" }
                ans[i + j] = s2[j]
            }
        }
        for i in 0..<L where ans[i] == "?" { ans[i] = "a" }
        for i in 0..<n where s1[i] == "F" {
            var match = true
            for j in 0..<m where ans[i + j] != s2[j] { match = false; break }
            if match {
                var changed = false
                for j in stride(from: m - 1, through: 0, by: -1) {
                    let pos = i + j
                    var forced = false
                    for t in 0..<n {
                        if s1[t] == "T" && pos >= t && pos < t + m { forced = true; break }
                    }
                    if !forced {
                        ans[pos] = "b"
                        changed = true
                        break
                    }
                }
                if !changed { return "" }
            }
        }
        for i in 0..<n {
            var match = true
            for j in 0..<m where ans[i + j] != s2[j] { match = false; break }
            if s1[i] == "T" && !match { return "" }
            if s1[i] == "F" && match { return "" }
        }
        return String(ans)
    }
}
