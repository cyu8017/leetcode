// LeetCode 1921 - Eliminate Maximum Number Of Monsters
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

class Solution {
    fun eliminateMaximum(dist: IntArray, speed: IntArray): Int {
        val arrival = IntArray(dist.size) { i -> (dist[i] + speed[i] - 1) / speed[i] }
        arrival.sort()
        for (i in arrival.indices) if (arrival[i] <= i) return i
        return arrival.size
    }
}
