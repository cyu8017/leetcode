// LeetCode 2278 - Percentage of Letter in String
// https://leetcode.com/problems/percentage-of-letter-in-string/

class Solution {
    func percentageLetter(_ s: String, _ letter: Character) -> Int {
        s.filter { $0 == letter }.count * 100 / s.count
    }
}
