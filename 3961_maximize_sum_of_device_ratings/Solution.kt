// LeetCode 3961 - Maximize Sum Of Device Ratings
// https://leetcode.com/problems/maximize-sum-of-device-ratings/

class Solution {
    fun maxRatings(units: Array<IntArray>): Long {
        var n = units[0].size
        if (n == 1) {
            var ans = 0
            for (x in units) ans += x[0]
            return ans
        }
        var answer = 0
        var mn = Int.MAX_VALUE
        var mn2 = Int.MAX_VALUE
        for (x in units) {
            x.sort()
            answer += x[1]
            mn2 = minOf(mn2, x[1])
            mn = minOf(mn, x[0])
        }
        return answer - (mn2 - mn)
    }
}
