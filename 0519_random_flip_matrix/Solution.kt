// LeetCode 0519 - Random Flip Matrix
// https://leetcode.com/problems/random-flip-matrix/

object Uniform {
    private var uniformFn: (Double, Double) -> Double = { a, _ -> a }
    private var sequence: Iterator<Double> = emptyList<Double>().iterator()

    fun setSequence(values: DoubleArray) {
        sequence = values.toList().iterator()
        uniformFn = { _, _ -> sequence.next() }
    }

    fun set_uniform(fn: (Double, Double) -> Double) {
        uniformFn = fn
    }

    fun setUniform(fn: (Double, Double) -> Double) = set_uniform(fn)

    fun uniform(a: Double, b: Double): Double = uniformFn(a, b)
}

class Solution(m: Int, n: Int) {
    private val cols = n
    private val total = m * n
    private var available = mutableListOf<Int>()

    init {
        reset()
    }

    fun flip(): IntArray {
        var index = Uniform.uniform(0.0, (available.size - 1).toDouble()).toInt()
        if (index >= available.size) {
            index = available.size - 1
        }
        val value = available[index]
        available[index] = available.last()
        available.removeAt(available.lastIndex)
        return intArrayOf(value / cols, value % cols)
    }

    fun reset() {
        available = (0 until total).toMutableList()
    }
}
