// LeetCode 3096 - Minimum Levels to Gain More Points
// https://leetcode.com/problems/minimum-levels-to-gain-more-points/

class Solution {
    fun minimumLevels(possible: IntArray): Int {
        var s = 0
        for (x in possible) { s += (x == 0 ? -1 : x) }
        var t = 0
        var i = 0
        while (i + 1 < possible.size) {
            var x = if (possible[i] == 0) -1 else possible[i]
            t += x
            if (t > s - t) return i + 1
            i++
        }
        return -1
    }
}
