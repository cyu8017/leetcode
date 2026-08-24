// LeetCode 0528 - Random Pick with Weight
// https://leetcode.com/problems/random-pick-with-weight/

object Uniform {
    private var uniformFn: (Double, Double) -> Double = { _, _ -> 0.0 }
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

class Solution(w: IntArray) {
    private val prefix: IntArray
    private val total: Int

    init {
        var runningTotal = 0
        prefix = IntArray(w.size) { index ->
            runningTotal += w[index]
            runningTotal
        }
        total = runningTotal
    }

    fun pickIndex(): Int {
        var target = Uniform.uniform(0.0, total.toDouble()).toInt()
        if (target >= total) {
            target = total - 1
        }
        return bisectRight(prefix, target)
    }

    private fun bisectRight(values: IntArray, target: Int): Int {
        var low = 0
        var high = values.size - 1
        while (low < high) {
            val mid = (low + high) / 2
            if (values[mid] <= target) {
                low = mid + 1
            } else {
                high = mid
            }
        }
        return low
    }
}
