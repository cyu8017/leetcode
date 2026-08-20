// LeetCode 1422 - Maximum Score After Splitting a String
// https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution {
    func maxScore(_ s: String) -> Int {
        var ones = s.filter { $0 == "1" }.count
        var leftZeros = 0, answer = 0
        let chars = Array(s)
        for char in chars.dropLast() {
            if char == "0" { leftZeros += 1 } else { ones -= 1 }
            answer = max(answer, leftZeros + ones)
        }
        return answer
    }
}
