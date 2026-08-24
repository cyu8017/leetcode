// LeetCode 2055 - Plates Between Candles
// https://leetcode.com/problems/plates-between-candles/

class Solution {
    func platesBetweenCandles(_ s: String, _ queries: [[Int]]) -> [Int] {
        let chars = Array(s)
        let n = chars.count
        var pref = [Int](repeating: 0, count: n + 1)
        var left = [Int](repeating: -1, count: n)
        var right = [Int](repeating: -1, count: n)
        var last = -1
        for i in 0..<n {
            pref[i + 1] = pref[i] + (chars[i] == "*" ? 1 : 0)
            if chars[i] == "|" { last = i }
            left[i] = last
        }
        last = -1
        for i in stride(from: n - 1, through: 0, by: -1) {
            if chars[i] == "|" { last = i }
            right[i] = last
        }
        return queries.map { q in
            let l = right[q[0]], r = left[q[1]]
            if l != -1 && r != -1 && l < r { return pref[r] - pref[l] }
            return 0
        }
    }
}
