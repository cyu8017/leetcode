// LeetCode 3773 - Maximum Number Of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

class Solution {
    func maxSameLengthRuns(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var cnt = [Int: Int]()
        var ans = 0
        var i = 0
        while i < n {
            var j = i + 1
            while j < n && chars[j] == chars[i] { j += 1 }
            let m = j - i
            cnt[m, default: 0] += 1
            ans = max(ans, cnt[m]!)
            i = j
        }
        return ans
    }
}
