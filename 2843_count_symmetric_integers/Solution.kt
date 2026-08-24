// LeetCode 2843 - Count Symmetric Integers
// https://leetcode.com/problems/count-symmetric-integers/

class Solution {
    fun countSymmetricIntegers(low: Int, high: Int): Int {
        var ans = 0
        for (x in low..high) {
            val s = x.toString()
            if (s.length % 2 != 0) continue
            val mid = s.length / 2
            var a = 0
            var b = 0
            for (i in 0 until mid) {
                a += s[i] - '0'
                b += s[mid + i] - '0'
            }
            if (a == b) ans++
        }
        return ans
    }
}
