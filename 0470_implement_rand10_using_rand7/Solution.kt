// LeetCode 0470 - Implement Rand10() Using Rand7()
// https://leetcode.com/problems/implement-rand10-using-rand7/

object Rand7 {
    private var sequence: Iterator<Int> = emptyList<Int>().iterator()

    fun setSequence(values: IntArray) {
        sequence = values.toList().iterator()
    }

    fun rand7(): Int = sequence.next()
}

class Solution {
    fun rand10(): Int {
        while (true) {
            val num = (Rand7.rand7() - 1) * 7 + Rand7.rand7()
            if (num <= 40) {
                return (num - 1) % 10 + 1
            }
        }
    }
}
