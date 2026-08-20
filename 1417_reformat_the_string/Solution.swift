// LeetCode 1417 - Reformat The String
// https://leetcode.com/problems/reformat-the-string/

class Solution {
    func reformat(_ s: String) -> String {
        var letters = [Character](), digits = [Character]()
        for c in s {
            if c.isLetter { letters.append(c) } else { digits.append(c) }
        }
        if abs(letters.count - digits.count) > 1 { return "" }
        if digits.count >= letters.count { swap(&letters, &digits) }
        var answer = [Character]()
        for (i, char) in letters.enumerated() {
            answer.append(char)
            if i < digits.count { answer.append(digits[i]) }
        }
        return String(answer)
    }
}
