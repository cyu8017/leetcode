// LeetCode 1446 - Consecutive Characters
// https://leetcode.com/problems/consecutive-characters/

class Solution {
    func maxPower(_ s: String) -> Int {
        let chars = Array(s)
        var answer = 1, run = 1
        for i in 1..<chars.count {
            run = chars[i] == chars[i - 1] ? run + 1 : 1
            answer = max(answer, run)
        }
        return answer
    }
}
