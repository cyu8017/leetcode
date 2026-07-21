// LeetCode 1898 - Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

class Solution {
    fun maximumRemovals(s: String, p: String, removable: IntArray): Int {
        fun stillSubsequence(k: Int): Boolean {
            val removed = BooleanArray(s.length)
            for (i in 0 until k) removed[removable[i]] = true
            var index = 0
            for (position in s.indices) {
                if (removed[position]) continue
                if (index < p.length && s[position] == p[index]) index++
            }
            return index == p.length
        }
        var lo = 0
        var hi = removable.size
        while (lo < hi) {
            val mid = (lo + hi + 1) ushr 1
            if (stillSubsequence(mid)) lo = mid else hi = mid - 1
        }
        return lo
    }
}
