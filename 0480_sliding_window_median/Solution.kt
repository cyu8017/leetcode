// LeetCode 0480 - Sliding Window Median
// https://leetcode.com/problems/sliding-window-median/

class Solution {
    fun medianSlidingWindow(nums: IntArray, k: Int): DoubleArray {
        val window = nums.copyOfRange(0, k).sorted().toMutableList()
        val result = mutableListOf<Double>()
        appendMedian(window, k, result)

        for (index in k until nums.size) {
            val outgoing = nums[index - k]
            val incoming = nums[index]
            window.removeAt(window.binarySearch(outgoing))
            val insertPos = window.binarySearch(incoming).let { if (it < 0) -it - 1 else it }
            window.add(insertPos, incoming)
            appendMedian(window, k, result)
        }
        return result.toDoubleArray()
    }

    private fun appendMedian(window: List<Int>, k: Int, result: MutableList<Double>) {
        if (k % 2 == 1) {
            result.add(window[k / 2].toDouble())
        } else {
            result.add((window[k / 2 - 1] + window[k / 2]) / 2.0)
        }
    }
}
