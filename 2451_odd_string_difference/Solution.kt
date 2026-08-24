// LeetCode 2451 - Odd String Difference
// https://leetcode.com/problems/odd-string-difference/

class Solution {
    fun oddString(words: Array<String>): String {
        val d0 = diff(words[0])
        val d1 = diff(words[1])
        if (d0 == d1) {
            for (i in 2 until words.size) {
                if (diff(words[i]) != d0) return words[i]
            }
        }
        return if (diff(words[2]) == d0) words[1] else words[0]
    }

    private fun diff(w: String): String {
        val b = StringBuilder()
        for (i in 1 until w.length) {
            val d = w[i] - w[i - 1]
            b.append((d + 128).toChar())
            b.append(',')
        }
        return b.toString()
    }
}
