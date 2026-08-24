// LeetCode 3495 - Minimum Operations to Make Array Elements Zero
// https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/

class Solution {
    private fun opsToZero(x: Int): Int {
        var ops = 0
        while (x > 0) { x /= 4; ops++; }
        return ops
    }

    fun minOperations(queries: Array<IntArray>): Long {
        var ans = 0
        for (q in queries) {
            var l = q[0]
            var r = q[1]
            var sum = 0
            for (x in l .. r) { sum += opsToZero(x) }
            ans += (sum + 1) / 2
        }
        return ans
    }
}
