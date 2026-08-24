// LeetCode 3923 - Minimum Generations to Target Point
// https://leetcode.com/problems/minimum-generations-to-target-point/

data class P(val a: Int, val b: Int, val c: Int)

class Solution {
    fun minGenerations(points: Array<IntArray>, target: IntArray): Int {
        val targetPoint = P(target[0], target[1], target[2])
        val generation = HashMap<P, Int>()
        val all = ArrayList<P>()
        for (values in points) {
            val p = P(values[0], values[1], values[2])
            generation[p] = 0
            all.add(p)
        }
        if (generation.containsKey(targetPoint)) return generation[targetPoint]!!
        var current = 1
        while (true) {
            val limit = all.size
            val added = ArrayList<P>()
            for (i in 0 until limit) {
                for (j in i + 1 until limit) {
                    if (all[i] == all[j]) continue
                    val pi = all[i]
                    val pj = all[j]
                    val p = P((pi.a + pj.a) / 2, (pi.b + pj.b) / 2, (pi.c + pj.c) / 2)
                    if (!generation.containsKey(p)) {
                        generation[p] = current
                        added.add(p)
                    }
                }
            }
            if (generation.containsKey(targetPoint)) return generation[targetPoint]!!
            if (added.isEmpty()) return -1
            all.addAll(added)
            current++
        }
    }
}
