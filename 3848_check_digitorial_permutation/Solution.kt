// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

class Solution {
    fun isDigitorialPermutation(n: Int): Boolean {
        var f = IntArray(10)
        f[0] = 1
        for (i in 1 until 10) { f[i] = f[i - 1] * i }
        var x = 0
        var y = n
        while (y > 0) {
            x += f[y % 10]
            y /= 10
        }
        var a = x.toString().toCharArray()
        var b = n.toString().toCharArray()
        a.sort()
        b.sort()
        return String((a) == String(b))
    }
}
