// LeetCode 1017 - Convert to Base -2
// https://leetcode.com/problems/convert-to-base-2/

class Solution {
    fun baseNeg2(n: Int): String {
        if (n == 0) return "0"
        val ans = StringBuilder()
        var cur = n
        while (cur != 0) {
            var rem = cur % -2
            cur /= -2
            if (rem < 0) {
                cur++
                rem += 2
            }
            ans.append(rem)
        }
        return ans.reverse().toString()
    }
}
