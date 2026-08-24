// LeetCode 2024 - Maximize the Confusion of an Exam
// https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution {
    func maxConsecutiveAnswers(_ answerKey: String, _ k: Int) -> Int {
        let chars = Array(answerKey)
        return max(maxWith(chars, k, "T"), maxWith(chars, k, "F"))
    }

    private func maxWith(_ chars: [Character], _ k: Int, _ ch: Character) -> Int {
        var left = 0, bad = 0, best = 0
        for right in 0..<chars.count {
            if chars[right] != ch { bad += 1 }
            while bad > k {
                if chars[left] != ch { bad -= 1 }
                left += 1
            }
            best = max(best, right - left + 1)
        }
        return best
    }
}
