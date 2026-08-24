// LeetCode 2264 - Largest 3-Same-Digit Number in String
// https://leetcode.com/problems/largest-3-same-digit-number-in-string/

class Solution {

    fun largestGoodInteger(num: String): String {

            var best = ""
            run {
    var i = 0
    while (i + 2 < num.length) {

                if (num[i] == num[i + 1] && num[i] == num[i + 2]) {
                    var cand = num.substring(i, i + 3)
                    if (cand.compareTo(best) > 0) best = cand
                }

    i++
    }
    }
            return best

    }

}
