// LeetCode 3208 - Alternating Groups II
// https://leetcode.com/problems/alternating-groups-ii/

class Solution {
    fun numberOfAlternatingGroups(colors: IntArray, k: Int): Int {
        var n = colors.size
        var cnt = 0
        var ans = 0
        for (i in 0 until n * 2) {
            if (i > 0 && colors[i % n] == colors[(i - 1) % n]) cnt = 1
            else cnt++
            if (i >= n && cnt >= k) ans++
        }
        return ans
    }
}
