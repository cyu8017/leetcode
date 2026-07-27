// LeetCode 1625 - Lexicographically Smallest String After Applying Operations
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

class Solution {
    fun findLexSmallestString(s: String, a: Int, b: Int): String {
        val seen = HashSet<String>()
        val q = ArrayDeque<String>()
        seen.add(s)
        q.add(s)
        var ans = s
        while (q.isNotEmpty()) {
            val cur = q.removeFirst()
            if (cur < ans) ans = cur
            val chars = cur.toCharArray()
            for (i in chars.indices) {
                if (i % 2 == 1) chars[i] = '0' + (chars[i] - '0' + a) % 10
            }
            val add = String(chars)
            val rot = cur.substring(cur.length - b) + cur.substring(0, cur.length - b)
            for (nxt in listOf(add, rot)) {
                if (seen.add(nxt)) q.add(nxt)
            }
        }
        return ans
    }
}
