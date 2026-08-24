// LeetCode 4008 - Minimum Initial Strength to Defeat All Monsters
// https://leetcode.com/problems/minimum-initial-strength-to-defeat-all-monsters/

class Solution {
    fun minInitialStrength(monsters: IntArray, boosts: Array<IntArray>): Long {
        var n = monsters.size
        var d = LongArray(n + 1)
        for (b in boosts) {
            d[b[0]] += b[2]
            d[b[1] + 1] -= b[2]
        }
        var left = 0
        var right = 1000000000000000L
        while (left < right) {
            var mid = (left + right) / 2
            if (check(mid, monsters, d)) right = mid
            else left = mid + 1
        }
        return left
    }

    private fun check(v: Long, monsters: IntArray, d: LongArray): Boolean {
        var bonus = 0
        for (i in 0 until monsters.size) {
            bonus += d[i]
            if (v + bonus < monsters[i]) return false
            v -= monsters[i]
            if (v < 0) v = 0
        }
        return true
    }
}
