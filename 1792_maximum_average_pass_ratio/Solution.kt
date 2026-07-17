// LeetCode 1792 - Maximum Average Pass Ratio
// https://leetcode.com/problems/maximum-average-pass-ratio/

import java.util.PriorityQueue

class Solution {
    fun maxAverageRatio(classes: Array<IntArray>, extraStudents: Int): Double {
        fun gain(p: Double, t: Double) = (p + 1) / (t + 1) - p / t

        val heap = PriorityQueue<DoubleArray>(compareByDescending { it[0] })
        for (cls in classes) {
            val p = cls[0].toDouble()
            val t = cls[1].toDouble()
            heap.offer(doubleArrayOf(gain(p, t), p, t))
        }
        repeat(extraStudents) {
            val top = heap.poll()
            val p = top[1] + 1
            val t = top[2] + 1
            heap.offer(doubleArrayOf(gain(p, t), p, t))
        }
        var total = 0.0
        for (entry in heap) {
            total += entry[1] / entry[2]
        }
        return total / classes.size
    }
}
