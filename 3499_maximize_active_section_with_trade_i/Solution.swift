// LeetCode 3499 - Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/

class Solution {
    func maxActiveSectionsAfterTrade(_ s: String) -> Int {
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
        var best = 0
        if zeros.count >= 2 {
            for i in 0..<(zeros.count - 1) {
                let gain = (zeros[i][1] - zeros[i][0] + 1) + (zeros[i + 1][1] - zeros[i + 1][0] + 1)
                if gain > best { best = gain }
            }
        }
        return ones + best
    }
}
