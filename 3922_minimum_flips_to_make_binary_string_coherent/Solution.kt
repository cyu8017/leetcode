// LeetCode 3922 - Minimum Flips to Make Binary String Coherent
// https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/

class Solution {
    fun minFlips(s: String): Int {
        var ones = 0
        for (c in s.toCharArray()) { if (c == '1') ones++ }
        var answer = ones
        if (ones > 0) answer = ones - 1
        var zeros = s.length - ones
        answer = minOf(answer, zeros)
        if (s.length >= 2) {
            var cost = 0
            for (i in 0 until s.length) {
                var want = if ((i == 0 || i == s.length - 1)) '1' else '0'
                if (s[i] != want) cost++
            }
            answer = minOf(answer, cost)
        }
        return answer
    }
}
