// LeetCode 0067 - Add Binary
// https://leetcode.com/problems/add-binary/

class Solution {
    fun addBinary(a: String, b: String): String {
        var i = a.length - 1
        var j = b.length - 1
        var carry = 0
        val result = StringBuilder()

        while (i >= 0 || j >= 0 || carry != 0) {
            var total = carry
            if (i >= 0) {
                total += a[i] - '0'
                i--
            }
            if (j >= 0) {
                total += b[j] - '0'
                j--
            }
            result.append(total % 2)
            carry = total / 2
        }

        return result.reverse().toString()
    }
}
