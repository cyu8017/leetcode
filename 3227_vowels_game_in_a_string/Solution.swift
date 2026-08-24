// LeetCode 3227 - Vowels Game in a String
// https://leetcode.com/problems/vowels-game-in-a-string/

class Solution {
    func doesAliceWin(_ s: String) -> Bool {
        for c in s where "aeiou".contains(c) { return true }
        return false
    }
}
