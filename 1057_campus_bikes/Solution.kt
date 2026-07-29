// LeetCode 1057 - Campus Bikes
// https://leetcode.com/problems/campus-bikes/

class Solution {
    fun assignBikes(workers: Array<IntArray>, bikes: Array<IntArray>): IntArray {
        val triples = mutableListOf<IntArray>()
        for (w in workers.indices) {
            for (b in bikes.indices) {
                val d = kotlin.math.abs(workers[w][0] - bikes[b][0]) +
                    kotlin.math.abs(workers[w][1] - bikes[b][1])
                triples.add(intArrayOf(d, w, b))
            }
        }
        triples.sortWith(compareBy({ it[0] }, { it[1] }, { it[2] }))
        val ans = IntArray(workers.size) { -1 }
        val usedBikes = BooleanArray(bikes.size)
        var assigned = 0
        for (t in triples) {
            if (ans[t[1]] == -1 && !usedBikes[t[2]]) {
                ans[t[1]] = t[2]
                usedBikes[t[2]] = true
                assigned++
                if (assigned == workers.size) break
            }
        }
        return ans
    }
}
