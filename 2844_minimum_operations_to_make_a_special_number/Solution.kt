// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

class Solution {
    fun minimumOperations(num: String): Int {
        val n = num.length
        var ans = n
        var has0 = false
        for (i in 0 until n) if (num[i] == '0') has0 = true
        if (has0) ans = minOf(ans, n - 1)
        val targets = arrayOf("00", "25", "50", "75")
        for (t in targets) {
            var j = n - 1
            while (j >= 0 && num[j] != t[1]) j--
            if (j < 0) continue
            var i = j - 1
            while (i >= 0 && num[i] != t[0]) i--
            if (i < 0) continue
            ans = minOf(ans, n - i - 2)
        }
        return ans
    }
}
