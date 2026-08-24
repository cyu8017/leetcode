// LeetCode 3750 - Minimum Number Of Flips To Reverse Binary String
// https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

class Solution {
    fun minimumFlips(n: Int): Int {
        val s: String
        var x = n.toLong()
        if (x == 0L) {
            s = "0"
        } else {
            val sb = StringBuilder()
            while (x > 0) {
                sb.append(('0'.code + (x and 1).toInt()).toChar())
                x = x shr 1
            }
            val arr = sb.toString().toCharArray()
            reverse(arr)
            s = String(arr)
        }
        val m = s.length
        var cnt = 0
        for (i in 0 until m / 2) {
            if (s[i] != s[m - i - 1]) cnt++
        }
        return cnt * 2
    }

    private fun reverse(a: CharArray) {
        reverse(a, 0, a.size)
    }

    private fun reverse(a: CharArray, l: Int, r: Int) {
        var i = l
        var j = r - 1
        while (i < j) {
            val t = a[i]
            a[i] = a[j]
            a[j] = t
            i++
            j--
        }
    }
}
