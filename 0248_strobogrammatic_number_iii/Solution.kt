// LeetCode 0248 - Strobogrammatic Number III
// https://leetcode.com/problems/strobogrammatic-number-iii/

class Solution {
    private val pairs = arrayOf(
        "0" to "0",
        "1" to "1",
        "6" to "9",
        "8" to "8",
        "9" to "6",
    )

    fun strobogrammaticInRange(low: String, high: String): Int {
        val lowValue = low.toLong()
        val highValue = high.toLong()
        var count = 0

        for (length in low.length..high.length) {
            for (value in build(0, length - 1)) {
                val numeric = value.toLong()
                if (numeric in lowValue..highValue) {
                    count++
                }
            }
        }
        return count
    }

    private fun build(left: Int, right: Int): List<String> {
        if (left > right) {
            return listOf("")
        }
        if (left == right) {
            return listOf("0", "1", "8")
        }
        val result = mutableListOf<String>()
        for ((start, end) in pairs) {
            if (left == 0 && start == "0") {
                continue
            }
            for (middle in build(left + 1, right - 1)) {
                result.add(start + middle + end)
            }
        }
        return result
    }
}
