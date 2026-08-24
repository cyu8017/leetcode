// LeetCode 0825 - Friends Of Appropriate Ages
// https://leetcode.com/problems/friends-of-appropriate-ages/

class Solution {
    fun numFriendRequests(ages: IntArray): Int {
        var count = IntArray(121)
        for (age in ages) { count[age]++ }
        var ans = 0
        for (x in 1 until = 120) {
            if (count[x] == 0) continue
            for (y in 1 until = 120) {
                if (count[y] == 0) continue
                if (y <= 0.5 * x + 7 || y > x || (y > 100 && x < 100)) continue
                ans += count[x] * count[y]
                if (x == y) ans -= count[x]
            }
        }
        return ans
    }
}
