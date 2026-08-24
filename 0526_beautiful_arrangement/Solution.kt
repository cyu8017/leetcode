// LeetCode 0526 - Beautiful Arrangement
// https://leetcode.com/problems/beautiful-arrangement/

class Solution {
    fun countArrangement(n: Int): Int {
        return backtrack(1, n, mutableSetOf())
    }

    private fun backtrack(index: Int, n: Int, used: MutableSet<Int>): Int {
        if (index == n + 1) {
            return 1
        }
        var count = 0
        for (num in 1..n) {
            if (num in used) {
                continue
            }
            if (index % num == 0 || num % index == 0) {
                used.add(num)
                count += backtrack(index + 1, n, used)
                used.remove(num)
            }
        }
        return count
    }
}
