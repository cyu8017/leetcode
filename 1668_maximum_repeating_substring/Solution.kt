// LeetCode 1668 - Maximum Repeating Substring
// https://leetcode.com/problems/maximum-repeating-substring/

class Solution {
    fun maxRepeating(sequence: String, word: String): Int {
        var k = 0
        while (word.repeat(k + 1) in sequence) k++
        return k
    }
}
