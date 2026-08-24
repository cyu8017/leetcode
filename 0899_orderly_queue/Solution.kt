// LeetCode 0899 - Orderly Queue
// https://leetcode.com/problems/orderly-queue/

class Solution {
    fun orderlyQueue(s: String, k: Int): String {
        if (k > 1) {
            var chars = s.toCharArray()
            chars.sort()
            return String(chars)
        }
        var best = s
        for (i in 1 until s.length) {
            var cand = s.substring(i) + s.substring(0, i)
            if (cand.compareTo(best) < 0) best = cand
        }
        return best
    }
}
