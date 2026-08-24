// LeetCode 3340 - Check Balanced String
// https://leetcode.com/problems/check-balanced-string/

class Solution {
    func isBalanced(_ num: String) -> Bool {
        var even = 0, odd = 0
        for (i, c) in num.enumerated() {
            let d = Int(c.asciiValue! - 48)
            if i % 2 == 0 { even += d } else { odd += d }
        }
        return even == odd
    }
}
