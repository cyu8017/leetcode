// LeetCode 1642 - Furthest Building You Can Reach
// https://leetcode.com/problems/furthest-building-you-can-reach/

import java.util.PriorityQueue

class Solution {
    fun furthestBuilding(heights: IntArray, bricks: Int, ladders: Int): Int {
        val climbs = PriorityQueue<Int>()
        var remain = bricks
        for (i in 0 until heights.size - 1) {
            val d = heights[i + 1] - heights[i]
            if (d <= 0) continue
            climbs.offer(d)
            if (climbs.size > ladders) remain -= climbs.poll()
            if (remain < 0) return i
        }
        return heights.size - 1
    }
}
