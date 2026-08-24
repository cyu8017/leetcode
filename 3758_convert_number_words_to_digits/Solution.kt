// LeetCode 3758 - Convert Number Words To Digits
// https://leetcode.com/problems/convert_number_words_to_digits/

class Solution {
    fun convertNumber(s: String): String {
        var d = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
        var n = s.length
        var ans = StringBuilder()
        for (i in 0 until n) {
            for (j in 0 until 10) {
                var m = d[j].size
                if (i + m <= n && s.substring(i, i + (m) == d[j])) {
                    ans.append(('0' + j).toInt().toChar())
                    i += m - 1
                    break
                }
            }
        }
        return ans.toString()
    }
}
