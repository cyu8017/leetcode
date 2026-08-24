// LeetCode 2358 - Maximum Number of Groups Entering a Competition
// https://leetcode.com/problems/maximum-number-of-groups-entering-a-competition/

class Solution {
    fun maximumGroups(grades: IntArray): Int {
        val n = grades.size
        var k = 0
        while ((k + 1L) * (k + 2) / 2 <= n) k++
        return k
    }
}
