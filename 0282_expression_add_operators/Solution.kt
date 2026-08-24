// LeetCode 0282 - Expression Add Operators
// https://leetcode.com/problems/expression-add-operators/

class Solution {
    fun addOperators(num: String, target: Int): List<String> {
        val result = mutableListOf<String>()

        fun backtrack(index: Int, path: String, value: Long, previous: Long) {
            if (index == num.length) {
                if (value == target.toLong()) {
                    result.add(path)
                }
                return
            }
            for (end in index until num.length) {
                if (end > index && num[index] == '0') {
                    break
                }
                val currentStr = num.substring(index, end + 1)
                val current = currentStr.toLong()
                if (index == 0) {
                    backtrack(end + 1, currentStr, current, current)
                } else {
                    backtrack(end + 1, "$path+$currentStr", value + current, current)
                    backtrack(end + 1, "$path-$currentStr", value - current, -current)
                    backtrack(
                        end + 1,
                        "$path*$currentStr",
                        value - previous + previous * current,
                        previous * current,
                    )
                }
            }
        }

        backtrack(0, "", 0L, 0L)
        return result
    }
}
