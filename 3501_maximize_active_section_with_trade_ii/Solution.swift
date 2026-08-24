// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

class Solution {
    func maxActiveSectionsAfterTrade(_ s: String, _ queries: [[Int]]) -> [Int] {
        let chars = Array(s)
        var ones = 0
        for c in chars where c == "1" { ones += 1 }
        var zeros = [[Int]]()
        let n = chars.count
        var i = 0
        while i < n {
            if chars[i] != "0" { i += 1; continue }
            var j = i
            while j < n && chars[j] == "0" { j += 1 }
            zeros.append([i, j - 1])
            i = j
        }
        var ans = Array(repeating: ones, count: queries.count)
        for qi in 0..<queries.count {
            let L = queries[qi][0], R = queries[qi][1]
            var best = 0
            if zeros.count >= 2 {
                for i in 0..<(zeros.count - 1) {
                    let a = zeros[i], b = zeros[i + 1]
                    if a[0] >= L && b[1] <= R {
                        let gain = (a[1] - a[0] + 1) + (b[1] - b[0] + 1)
                        if gain > best { best = gain }
                    }
                }
            }
            ans[qi] = ones + best
        }
        return ans
    }
}
