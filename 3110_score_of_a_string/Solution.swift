// LeetCode 3110 - Score of a String
// https://leetcode.com/problems/score-of-a-string/

class Solution {
    func scoreOfString(_ s: String) -> Int {
        let chars = Array(s)
        var ans = 0
        for i in 1..<chars.count {
            ans += abs(Int(chars[i - 1].asciiValue!) - Int(chars[i].asciiValue!))
        }
        return ans
    }
}
