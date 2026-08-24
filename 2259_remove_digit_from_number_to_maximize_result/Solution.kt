// LeetCode 2259 - Remove Digit From Number to Maximize Result
// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

class Solution {

    fun removeDigit(number: String, digit: Char): String {

            var best = ""
            for (i in 0 until number.length) {
                if (number[i] == digit) {
                    var cand = number.substring(0, i) + number.substring(i + 1)
                    if (cand.compareTo(best) > 0) best = cand
                }
            }
            return best

    }

}
