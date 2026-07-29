// LeetCode 1093 - Statistics from a Large Sample
// https://leetcode.com/problems/statistics-from-a-large-sample/

class Solution {
    fun sampleStats(count: IntArray): DoubleArray {
        var total = 0
        for (c in count) total += c
        var minimum = 0
        for (i in 0 until 256) {
            if (count[i] > 0) {
                minimum = i
                break
            }
        }
        var maximum = 0
        for (i in 255 downTo 0) {
            if (count[i] > 0) {
                maximum = i
                break
            }
        }
        var sum = 0L
        for (i in 0 until 256) sum += i.toLong() * count[i]
        val mean = sum.toDouble() / total
        var mode = 0
        for (i in 1 until 256) {
            if (count[i] > count[mode]) mode = i
        }
        val mid1 = (total + 1) / 2
        val mid2 = (total + 2) / 2
        var seen = 0
        var first = -1
        var second = -1
        for (i in 0 until 256) {
            seen += count[i]
            if (first < 0 && seen >= mid1) first = i
            if (second < 0 && seen >= mid2) {
                second = i
                break
            }
        }
        val median = (first + second) / 2.0
        return doubleArrayOf(minimum.toDouble(), maximum.toDouble(), mean, median, mode.toDouble())
    }
}
