// LeetCode 0497 - Random Point in Non-overlapping Rectangles
// https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

object Uniform {
    private var sequence: Iterator<Double> = emptyList<Double>().iterator()

    fun setSequence(values: DoubleArray) {
        sequence = values.toList().iterator()
    }

    fun uniform(a: Double, b: Double): Double = sequence.next()
}

class Solution(rects: Array<IntArray>) {
    private val rects = rects
    private val total: Int

    init {
        var areaTotal = 0
        for (rect in rects) {
            val width = rect[2] - rect[0] + 1
            val height = rect[3] - rect[1] + 1
            areaTotal += width * height
        }
        total = areaTotal
    }

    fun pick(): IntArray {
        var index = Uniform.uniform(0.0, total.toDouble()).toInt()
        if (index >= total) index = total - 1
        for (rect in rects) {
            val width = rect[2] - rect[0] + 1
            val height = rect[3] - rect[1] + 1
            val size = width * height
            if (index < size) {
                val offsetX = index % width
                val offsetY = index / width
                return intArrayOf(rect[0] + offsetX, rect[1] + offsetY)
            }
            index -= size
        }
        val last = rects.last()
        return intArrayOf(last[0], last[1])
    }
}
