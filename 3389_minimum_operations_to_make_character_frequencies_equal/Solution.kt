// LeetCode 3389 - Minimum Operations to Make Character Frequencies Equal
// https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/

class Solution {
    fun makeStringGood(s: String): Int {
        var freq = IntArray(26)
        for (c in s.toCharArray()) { freq[c - 'a'] = freq[c - 'a'] + 1 }
        var ans = s.length
        for (t in 1 ..s.length) {
            var pool = 0
            for (i in 0 until 26) { if (freq[i] > t) pool += freq[i] - t }
            var deficit = 0
            for (i in 0 until 26) { if (freq[i] < t) deficit += t - freq[i] }
            var ops = maxOf(pool, deficit)
            if (ops < ans) ans = ops
        }
        if (s.length < ans) ans = s.length
        return ans
    }
}
