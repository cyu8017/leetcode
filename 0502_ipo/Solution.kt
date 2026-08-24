// LeetCode 0502 - IPO
// https://leetcode.com/problems/ipo/

import java.util.PriorityQueue

class Solution {
    fun findMaximizedCapital(k: Int, w: Int, profits: IntArray, capital: IntArray): Int {
        val projects = capital.indices.map { index -> capital[index] to profits[index] }.sortedBy { it.first }
        val available = PriorityQueue<Int>(compareByDescending { it })
        var wealth = w
        var projectIndex = 0
        repeat(k) {
            while (projectIndex < projects.size && projects[projectIndex].first <= wealth) {
                available.offer(projects[projectIndex].second)
                projectIndex++
            }
            if (available.isEmpty()) return@repeat
            wealth += available.poll()
        }
        return wealth
    }
}
