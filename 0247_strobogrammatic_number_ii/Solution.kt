// LeetCode 0247 - Strobogrammatic Number II
// https://leetcode.com/problems/strobogrammatic-number-ii/

class Solution {
    private val pairs = arrayOf(
        "0" to "0",
        "1" to "1",
        "6" to "9",
        "8" to "8",
        "9" to "6",
    )

    fun findStrobogrammatic(n: Int): List<String> {
        return build(0, n - 1)
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
