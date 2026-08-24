// LeetCode 3280 - Convert Date to Binary
// https://leetcode.com/problems/convert-date-to-binary/

class Solution {
    fun convertDateToBinary(date: String): String {
        val parts = date.split("-")
        val y = parts[0].toInt()
        val m = parts[1].toInt()
        val d = parts[2].toInt()
        return toBinary(y) + "-" + toBinary(m) + "-" + toBinary(d)
    }

    private fun toBinary(v0: Int): String {
        var v = v0
        if (v == 0) return "0"
        val s = StringBuilder()
        while (v > 0) {
            s.insert(0, ('0'.code + (v and 1)).toChar())
            v = v shr 1
        }
        return s.toString()
    }
}
