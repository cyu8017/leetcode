// LeetCode 0466 - Count The Repetitions
// https://leetcode.com/problems/count-the-repetitions/

class Solution {
    fun getMaxRepetitions(s1: String, n1: Int, s2: String, n2: Int): Int {
        if (s2.isEmpty()) {
            return 0
        }

        var index = 0
        var s2Count = 0
        val record = mutableMapOf<Int, Pair<Int, Int>>()

        for (repeat in 0 until n1) {
            for (char in s1) {
                if (char == s2[index]) {
                    index++
                    if (index == s2.length) {
                        index = 0
                        s2Count++
                    }
                }
            }
            if (record.containsKey(index)) {
                val (previousRepeat, previousCount) = record[index]!!
                val cycle = repeat - previousRepeat
                val countCycle = s2Count - previousCount
                val remaining = n1 - repeat - 1
                s2Count += (remaining / cycle) * countCycle
                if (repeat + (remaining / cycle) * cycle >= n1 - 1) {
                    break
                }
            }
            record[index] = repeat to s2Count
        }

        return s2Count / n2
    }
}
