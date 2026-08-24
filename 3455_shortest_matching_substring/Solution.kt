// LeetCode 3455 - Shortest Matching Substring
// https://leetcode.com/problems/shortest-matching-substring/

class Solution {
    fun shortestMatchingSubstring(s: String, p: String): Int {
        val parts = ArrayList<String>()
        val cur = StringBuilder()
        for (ch in p) {
            if (ch == '*') {
                parts.add(cur.toString())
                cur.setLength(0)
            } else cur.append(ch)
        }
        parts.add(cur.toString())
        while (parts.size < 3) parts.add("")
        val a = parts[0]
        val b = parts[1]
        val c = parts[2]
        val n = s.length
        val posA = findAll(s, a)
        val posB = findAll(s, b)
        val posC = findAll(s, c)
        var ans = n + 1
        for (ia in posA) {
            val endA = ia + a.length
            var bi = sortSearch(posB, endA)
            while (bi < posB.size) {
                val endB = posB[bi] + b.length
                val ci = sortSearch(posC, endB)
                if (ci < posC.size) {
                    val length = posC[ci] + c.length - ia
                    if (length < ans) ans = length
                }
                break
            }
        }
        return if (ans == n + 1) -1 else ans
    }

    private fun findAll(s: String, sub: String): MutableList<Int> {
        val res = ArrayList<Int>()
        val n = s.length
        if (sub.isEmpty()) {
            for (i in 0..n) res.add(i)
            return res
        }
        var i = 0
        while (i + sub.length <= n) {
            if (s.regionMatches(i, sub, 0, sub.length)) res.add(i)
            i++
        }
        return res
    }

    private fun sortSearch(arr: MutableList<Int>, x: Int): Int {
        val i = arr.binarySearch(x)
        return if (i >= 0) i else -i - 1
    }
}
