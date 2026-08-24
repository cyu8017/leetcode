// LeetCode 3441 - Minimum Cost Good Caption
// https://leetcode.com/problems/minimum-cost-good-caption/

class Solution {
    func minCostGoodCaption(_ caption: String) -> String {
        var ans = Array(caption)
        let n = ans.count
        if n < 3 { return "" }
        var i = 0
        while i < n {
            var j = i
            while j < n && ans[j] == ans[i] { j += 1 }
            if j - i >= 3 { i = j; continue }
            let need = 3 - (j - i)
            if j + need <= n {
                for t in 0..<need { ans[j + t] = ans[i] }
                i = j + need
            } else {
                var ch: Character = "a"
                if i > 0 { ch = ans[i - 1] }
                else if j < n { ch = Array(caption)[j] }
                for t in i..<n { ans[t] = ch }
                break
            }
        }
        i = 0
        while i < n {
            var j = i
            while j < n && ans[j] == ans[i] { j += 1 }
            if j - i < 3 { return "" }
            i = j
        }
        return String(ans)
    }
}
