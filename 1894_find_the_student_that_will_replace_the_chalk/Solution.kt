// LeetCode 1894 - Find the Student that Will Replace the Chalk
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

class Solution {
    fun chalkReplacer(chalk: IntArray, k: Int): Int {
        var remaining = k.toLong() % chalk.sumOf { it.toLong() }
        for (index in chalk.indices) {
            if (remaining < chalk[index]) return index
            remaining -= chalk[index]
        }
        return 0
    }
}
