// LeetCode 0517 - Super Washing Machines
// https://leetcode.com/problems/super-washing-machines/

class Solution {
    fun findMinMoves(machines: IntArray): Int {
        val total = machines.sum()
        val count = machines.size
        if (total % count != 0) {
            return -1
        }
        val target = total / count
        var prefix = 0
        var result = 0
        for (clothes in machines) {
            val diff = clothes - target
            prefix += diff
            result = maxOf(result, kotlin.math.abs(prefix), diff)
        }
        return result
    }
}
