// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution {
    fun balancedStringSplit(s: String): Int {
        var balance = 0
        var answer = 0
        for (ch in s) {
            balance += if (ch == 'L') 1 else -1
            if (balance == 0) answer++
        }
        return answer
    }
}
