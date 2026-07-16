// LeetCode 0422 - Valid Word Square
// https://leetcode.com/problems/valid-word-square/

class Solution {
    func validWordSquare(_ words: [String]) -> Bool {
        for row in 0..<words.count {
            let word = words[row]
            for col in 0..<word.count {
                if col >= words.count {
                    return false
                }
                let other = words[col]
                if row >= other.count {
                    return false
                }
                let left = word.index(word.startIndex, offsetBy: col)
                let right = other.index(other.startIndex, offsetBy: row)
                if word[left] != other[right] {
                    return false
                }
            }
        }
        return true
    }
}
