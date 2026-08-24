// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

class Solution {
    fun canMakePaliQueries(s: String, queries: Array<IntArray>): List<Boolean> {
        val prefix = IntArray(s.length + 1)
        var mask = 0
        for (i in s.indices) {
            mask = mask xor (1 shl (s[i] - 'a'))
            prefix[i + 1] = mask
        }
        return queries.map { q ->
            val bits = Integer.bitCount(prefix[q[1] + 1] xor prefix[q[0]])
            bits / 2 <= q[2]
        }
    }
}
