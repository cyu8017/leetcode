// LeetCode 0434 - Number of Segments in a String
// https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution {
    fun countSegments(s: String): Int {
        var count = 0
        var inSegment = false
        for (char in s) {
            if (char != ' ') {
                if (!inSegment) {
                    count++
                    inSegment = true
                }
            } else {
                inSegment = false
            }
        }
        return count
    }
}
