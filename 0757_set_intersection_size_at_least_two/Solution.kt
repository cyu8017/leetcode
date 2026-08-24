// LeetCode 0757 - Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/

class Solution {
    fun intersectionSizeTwo(intervals: Array<IntArray>): Int {
        intervals.sortWith { a, b ->
            if (a[1] != b[1]) a[1].compareTo(b[1]) else a[0].compareTo(b[0])
        }
        var size = 0
        var first = -1
        var second = -1
        for (interval in intervals) {
            val left = interval[0]
            val right = interval[1]
            if (left <= first) continue
            if (left <= second) {
                size++
                first = second
                second = right
            } else {
                size += 2
                first = right - 1
                second = right
            }
        }
        return size
    }
}
