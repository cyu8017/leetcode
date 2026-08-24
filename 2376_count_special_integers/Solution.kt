// LeetCode 2376 - Count Special Integers
// https://leetcode.com/problems/count-special-integers/

class Solution {
    fun countSpecialNumbers(n: Int): Int {
        val s = n.toString()
        val m = s.length
        var ans = 0
        var perm = 9
        for (i in 1 until m) {
            ans += perm
            perm *= (10 - i)
        }
        val used = BooleanArray(10)
        for (i in 0 until m) {
            val start = if (i == 0) 1 else 0
            val digit = s[i] - '0'
            for (d in start until digit) {
                if (used[d]) continue
                var rem = 10 - (i + 1)
                var ways = 1
                for (j in i + 1 until m) {
                    ways *= rem
                    rem--
                }
                ans += ways
            }
            if (used[digit]) return ans
            used[digit] = true
        }
        return ans + 1
    }
}
