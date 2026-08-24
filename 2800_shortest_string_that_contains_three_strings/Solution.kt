// LeetCode 2800 - Shortest String That Contains Three Strings
// https://leetcode.com/problems/shortest-string-that-contains-three-strings/

class Solution {
    fun minimumString(a: String, b: String, c: String): String {
        val perms = arrayOf(
            arrayOf(a, b, c), arrayOf(a, c, b), arrayOf(b, a, c),
            arrayOf(b, c, a), arrayOf(c, a, b), arrayOf(c, b, a)
        )
        var ans = ""
        for (p in perms) {
            val cur = merge(merge(p[0], p[1]), p[2])
            if (ans.isEmpty() || cur.length < ans.length
                || (cur.length == ans.length && cur < ans)
            ) {
                ans = cur
            }
        }
        return ans
    }

    private fun merge(x: String, y: String): String {
        if (x.contains(y)) return x
        var best = x + y
        val n = minOf(x.length, y.length)
        for (i in n downTo 1) {
            if (x.substring(x.length - i) == y.substring(0, i)) {
                val cand = x + y.substring(i)
                if (cand.length < best.length || (cand.length == best.length && cand < best)) {
                    best = cand
                }
                break
            }
        }
        return best
    }
}
