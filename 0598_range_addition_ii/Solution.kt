// LeetCode 0598 - Range Addition II
// https://leetcode.com/problems/range-addition-ii/


class Solution {
    fun maxCount(m: Int, n: Int, ops: Array<IntArray>): Int {
        var rows = m
        var cols = n
        for (op in ops) {
            rows = minOf(rows, op[0])
            cols = minOf(cols, op[1])
        }
        return rows * cols
    }
}
