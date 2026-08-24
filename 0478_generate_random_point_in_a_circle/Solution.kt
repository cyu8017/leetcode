// LeetCode 0478 - Generate Random Point in a Circle
// https://leetcode.com/problems/generate-random-point-in-a-circle/

object Uniform {
    private var sequence: Iterator<Double> = emptyList<Double>().iterator()

    fun setSequence(values: DoubleArray) {
        sequence = values.toList().iterator()
    }

    fun uniform(a: Double, b: Double): Double = sequence.next()
}

class Solution(
    private val radius: Double,
    private val xCenter: Double,
    private val yCenter: Double,
) {
    fun randPoint(): DoubleArray {
        while (true) {
            val x = Uniform.uniform(-radius, radius)
            val y = Uniform.uniform(-radius, radius)
            if (x * x + y * y <= radius * radius) {
                return doubleArrayOf(
                    kotlin.math.round((xCenter + x) * 100000.0) / 100000.0,
                    kotlin.math.round((yCenter + y) * 100000.0) / 100000.0,
                )
            }
        }
    }
}
