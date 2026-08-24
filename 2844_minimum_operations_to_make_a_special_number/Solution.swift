// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

class Solution {
    func minimumOperations(_ num: String) -> Int {
        let chars = Array(num)
        let n = chars.count
        var ans = n
        if chars.contains("0") { ans = min(ans, n - 1) }
        for t in ["00", "25", "50", "75"] {
            let tArr = Array(t)
            var j = n - 1
            while j >= 0 && chars[j] != tArr[1] { j -= 1 }
            if j < 0 { continue }
            var i = j - 1
            while i >= 0 && chars[i] != tArr[0] { i -= 1 }
            if i < 0 { continue }
            ans = min(ans, n - i - 2)
        }
        return ans
    }
}
