// LeetCode 2145 - Count the Hidden Sequences
// https://leetcode.com/problems/count-the-hidden-sequences/

class Solution {
    func numberOfArrays(_ differences: [Int], _ lower: Int, _ upper: Int) -> Int {
        var cur = 0, mn = 0, mx = 0
        for d in differences {
            cur += d
            mn = min(mn, cur)
            mx = max(mx, cur)
        }
        let res = (upper - lower) - (mx - mn) + 1
        return res < 0 ? 0 : res
    }
}
