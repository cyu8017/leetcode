// LeetCode 2272 - Substring With Largest Variance
// https://leetcode.com/problems/substring-with-largest-variance/

class Solution {
    func largestVariance(_ s: String) -> Int {
        let arr = Array(s)
        var ans = 0
        for a in Character("a").asciiValue!...Character("z").asciiValue! {
            for b in Character("a").asciiValue!...Character("z").asciiValue! where a != b {
                var bal = 0
                var hasB = false
                for c in arr {
                    let v = c.asciiValue!
                    if v == a { bal += 1 }
                    else if v == b { bal -= 1; hasB = true }
                    if hasB { ans = max(ans, bal) }
                    if bal < 0 { bal = 0; hasB = false }
                }
            }
        }
        return ans
    }
}
