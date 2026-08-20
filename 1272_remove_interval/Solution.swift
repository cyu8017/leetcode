// LeetCode 1272 - Remove Interval
// https://leetcode.com/problems/remove-interval/

class Solution {
    func removeInterval(_ intervals: [[Int]], _ toBeRemoved: [Int]) -> [[Int]] {
        var ans: [[Int]] = []
        let a = toBeRemoved[0], b = toBeRemoved[1]
        for iv in intervals {
            let s = iv[0], e = iv[1]
            if e <= a || s >= b {
                ans.append(iv)
            } else {
                if s < a { ans.append([s, a]) }
                if e > b { ans.append([b, e]) }
            }
        }
        return ans
    }
}
