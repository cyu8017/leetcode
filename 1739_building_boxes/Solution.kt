// LeetCode 1739 - Building Boxes
// https://leetcode.com/problems/building-boxes/

class Solution {
    fun minimumBoxes(n: Int): Int {
        var height = 0L
        var used = 0L
        var base = 0L
        while (used + (height + 1) * (height + 2) / 2 <= n) {
            height++
            val layer = height * (height + 1) / 2
            used += layer
            base += height
        }
        var extra = 0L
        while (used < n) {
            extra++
            used += extra
        }
        return (base + extra).toInt()
    }
}
