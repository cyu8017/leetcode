// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

class Solution {
    func minFlips(_ s: String) -> Int {
        let chars = Array(s)
        var ones = 0
        for c in chars where c == "1" { ones += 1 }
        var answer = ones
        if ones > 0 { answer = ones - 1 }
        let zeros = chars.count - ones
        answer = min(answer, zeros)
        if chars.count >= 2 {
            var cost = 0
            for i in 0..<chars.count {
                let want: Character = (i == 0 || i == chars.count - 1) ? "1" : "0"
                if chars[i] != want { cost += 1 }
            }
            answer = min(answer, cost)
        }
        return answer
    }
}
