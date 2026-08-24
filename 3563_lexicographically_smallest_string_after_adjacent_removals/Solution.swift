// LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

class Solution {
    func lexicographicallySmallestString(_ s: String) -> String {
        let chars = Array(s)
        let n = chars.count
        var dp = Array(repeating: Array(repeating: "", count: n + 1), count: n + 1)
        if n == 0 { return "" }
        for length in 1...n {
            for i in 0...(n - length) {
                let j = i + length
                var minStr = String(chars[i]) + dp[i + 1][j]
                if i + 1 < j {
                    for k in (i + 1)..<j {
                        if isConsec(chars[i], chars[k]) && dp[i + 1][k].isEmpty {
                            let cand = dp[k + 1][j]
                            if cand < minStr { minStr = cand }
                        }
                    }
                }
                dp[i][j] = minStr
            }
        }
        return dp[0][n]
    }

    func isConsec(_ a: Character, _ b: Character) -> Bool {
        let d = abs(Int(a.asciiValue!) - Int(b.asciiValue!))
        return d == 1 || d == 25
    }
}
