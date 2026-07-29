// LeetCode 1056 - Confusing Number
// https://leetcode.com/problems/confusing-number/

class Solution {
    fun confusingNumber(n: Int): Boolean {
        val rotate = IntArray(10) { -1 }
        rotate[0] = 0
        rotate[1] = 1
        rotate[6] = 9
        rotate[8] = 8
        rotate[9] = 6
        val s = n.toString()
        val rotated = StringBuilder()
        for (i in s.lastIndex downTo 0) {
            val d = s[i] - '0'
            if (rotate[d] < 0) return false
            rotated.append(rotate[d])
        }
        return rotated.toString() != s
    }
}
