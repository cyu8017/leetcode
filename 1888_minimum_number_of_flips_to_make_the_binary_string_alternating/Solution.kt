// LeetCode 1888 - Minimum Number of Flips to Make the Binary String Alternating
// https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/

class Solution {
    fun minFlips(s: String): Int {
        val n = s.length
        val doubled = s + s
        var alt0 = 0
        var alt1 = 0
        for (i in 0 until n) {
            val expect0 = if (i % 2 == 0) '0' else '1'
            val expect1 = if (i % 2 == 0) '1' else '0'
            if (doubled[i] != expect0) alt0++
            if (doubled[i] != expect1) alt1++
        }
        var answer = minOf(alt0, alt1)
        for (i in 0 until n) {
            if (doubled[i] != if (i % 2 == 0) '0' else '1') alt0--
            if (doubled[i + n] != if ((i + n) % 2 == 0) '0' else '1') alt0++
            if (doubled[i] != if (i % 2 == 0) '1' else '0') alt1--
            if (doubled[i + n] != if ((i + n) % 2 == 0) '1' else '0') alt1++
            answer = minOf(answer, alt0, alt1)
        }
        return answer
    }
}
