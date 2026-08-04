// LeetCode 1954
// https://leetcode.com/problems/minimum-garden-perimeter-to-collect-enough-apples/

class Solution {
    fun minimumPerimeter(neededApples: Long): Long {
        var lo = 1L
        var hi = 100000L
        while (lo < hi) {
            val mid = (lo + hi) / 2
            val apples = 2 * mid * (mid + 1) * (2 * mid + 1)
            if (apples >= neededApples) hi = mid else lo = mid + 1
        }
        return 8 * lo
    }
}
