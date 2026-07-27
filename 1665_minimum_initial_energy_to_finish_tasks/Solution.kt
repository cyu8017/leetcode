// LeetCode 1665 - Minimum Initial Energy to Finish Tasks
// https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

class Solution {
    fun minimumEffort(tasks: Array<IntArray>): Int {
        tasks.sortByDescending { it[1] - it[0] }
        var energy = 0
        var spent = 0
        for (t in tasks) {
            energy = maxOf(energy, spent + t[1])
            spent += t[0]
        }
        return energy
    }
}
