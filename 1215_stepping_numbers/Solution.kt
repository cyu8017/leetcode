// LeetCode 1215 - Stepping Numbers
// https://leetcode.com/problems/stepping-numbers/

class Solution {
    fun countSteppingNumbers(low: Int, high: Int): List<Int> {
        val answer = mutableListOf<Int>()
        if (low == 0) answer.add(0)
        val q = ArrayDeque<Int>()
        for (i in 1..9) q.add(i)
        while (q.isNotEmpty()) {
            val x = q.removeFirst()
            if (x > high) continue
            if (x >= low) answer.add(x)
            val last = x % 10
            if (last > 0) {
                val next = x * 10L + last - 1
                if (next <= Int.MAX_VALUE) q.add(next.toInt())
            }
            if (last < 9) {
                val next = x * 10L + last + 1
                if (next <= Int.MAX_VALUE) q.add(next.toInt())
            }
        }
        return answer.sorted()
    }
}
