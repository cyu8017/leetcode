// LeetCode 0481 - Magical String
// https://leetcode.com/problems/magical-string/

class Solution {
    fun magicalString(n: Int): Int {
        if (n == 0) {
            return 0
        }
        val seq = mutableListOf(1, 2, 2)
        var index = 2
        while (seq.size < n) {
            val next = if (seq.last() == 2) 1 else 2
            if (seq[index] == 1) {
                seq.add(next)
            } else {
                seq.add(next)
                if (seq.size < n) {
                    seq.add(next)
                }
            }
            index += 1
        }
        return seq.take(n).count { it == 1 }
    }
}
