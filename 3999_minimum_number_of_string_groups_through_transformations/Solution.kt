// LeetCode 3999 - Minimum Number of String Groups Through Transformations
// https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/

class Solution {
    private fun leastRotation(s: String): Int {
        val n = s.length
        var i = 0
        var j = 1
        var k = 0
        while (i < n && j < n && k < n) {
            val a = s[(i + k) % n]
            val b = s[(j + k) % n]
            if (a == b) k++
            else {
                if (a > b) i += k + 1 else j += k + 1
                if (i == j) j++
                k = 0
            }
        }
        return if (i < j) i else j
    }

    private fun canonicalRotate(s: String): String {
        val n = s.length
        if (n <= 1) return s
        val r = leastRotation(s)
        if (r == 0) return s
        return s.substring(r) + s.substring(0, r)
    }

    fun minimumGroups(words: Array<String>): Int {
        val keys = ArrayList<String>()
        for (w in words) {
            val n = w.length
            val even = StringBuilder()
            val odd = StringBuilder()
            for (i in 0 until n) {
                if (i % 2 == 0) even.append(w[i]) else odd.append(w[i])
            }
            keys.add(canonicalRotate(even.toString()) + "#" + canonicalRotate(odd.toString()))
        }
        keys.sort()
        var groups = 0
        for (i in keys.indices) {
            if (i == 0 || keys[i] != keys[i - 1]) groups++
        }
        return groups
    }
}
