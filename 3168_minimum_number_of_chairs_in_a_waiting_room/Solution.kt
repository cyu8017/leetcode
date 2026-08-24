// LeetCode 3168 - Minimum Number of Chairs in a Waiting Room
// https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

class Solution {
    fun minimumChairs(s: String): Int {
        var cnt = 0
        var left = 0
        for (i in 0 until s.length) {
            var c = s[i]
            if (c == 'E') {
                if (left > 0) left--
                else cnt++
            } else left++
        }
        return cnt
    }
}
