// LeetCode 0686 - Repeated String Match
// https://leetcode.com/problems/repeated-string-match/

class Solution {
    fun repeatedStringMatch(a: String, b: String): Int {
        var repeats = (b.length + a.length - 1) / a.length
        var built = StringBuilder(a.length * (repeats + 1))
        for (i in 0 until repeats) { built.append(a) }
        if (built.toString().contains(b)) return repeats
        built.append(a)
        if (built.toString().contains(b)) return repeats + 1
        return -1
    }
}
