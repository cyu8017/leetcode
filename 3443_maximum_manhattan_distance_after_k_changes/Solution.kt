// LeetCode 3443 - Maximum Manhattan Distance After K Changes
// https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/

class Solution {
    fun maxDistance(s: String, k: Int): Int {
        var ans = 0
        var lat = 0
        var lon = 0
        for (i in 0 until s.length) {
            var c = s[i]
            if (c == 'N') lat++
            else if (c == 'S') lat--
            else if (c == 'E') lon++
            else lon--
            var md = kotlin.math.abs(lat) + kotlin.math.abs(lon)
            var steps = i + 1
            var cur = md + 2 * k
            if (cur > steps) cur = steps
            if (cur > ans) ans = cur
        }
        return ans
    }
}
