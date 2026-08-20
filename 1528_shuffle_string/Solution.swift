// LeetCode 1528 - Shuffle String
// https://leetcode.com/problems/shuffle-string/

class Solution {
    func restoreString(_ s: String, _ indices: [Int]) -> String {
        var answer = Array(repeating: Character(" "), count: s.count)
        for (ch, index) in zip(s, indices) {
            answer[index] = ch
        }
        return String(answer)
    }
}
