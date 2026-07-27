// LeetCode 1668 - Maximum Repeating Substring
// https://leetcode.com/problems/maximum-repeating-substring/

class Solution {
    func maxRepeating(_ sequence: String, _ word: String) -> Int {
        var k = 0
        while sequence.contains(String(repeating: word, count: k + 1)) {
            k += 1
        }
        return k
    }
}
