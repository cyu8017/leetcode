// LeetCode 3228 - Maximum Number of Operations to Move Ones to the End
// https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

class Solution {
    func maxOperations(_ s: String) -> Int {
        let chars = Array(s)
        var ans = 0, cnt = 0
        for i in 0..<chars.count {
            if chars[i] == "1" { cnt += 1 }
            else if i > 0 && chars[i - 1] == "1" { ans += cnt }
        }
        return ans
    }
}
