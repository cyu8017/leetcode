// LeetCode 3228 - Maximum Number of Operations to Move Ones to the End
// https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

class Solution {
    fun maxOperations(s: String): Int {
        var ans = 0
        var cnt = 0
        for (i in 0 until s.length) {
            if (s[i] == '1') cnt++
            else if (i > 0 && s[i - 1] == '1') ans += cnt
        }
        return ans
    }
}
