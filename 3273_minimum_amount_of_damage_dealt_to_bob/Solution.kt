// LeetCode 3273 - Minimum Amount of Damage Dealt to Bob
// https://leetcode.com/problems/minimum-amount-of-damage-dealt-to-bob/

class Solution {
    private class Enemy(val dmg: Int, val hits: Int)

    fun minDamage(power: Int, damage: IntArray, health: IntArray): Long {
        val n = damage.size
        val arr = Array(n) { i ->
            val hits = (health[i] + power - 1) / power
            Enemy(damage[i], hits)
        }
        var totalDmg = 0
        for (e in arr) totalDmg += e.dmg
        arr.sortWith { a, b ->
            (a.hits.toLong() * b.dmg).compareTo(b.hits.toLong() * a.dmg)
        }
        var ans = 0L
        var cur = totalDmg.toLong()
        for (e in arr) {
            ans += cur * e.hits
            cur -= e.dmg
        }
        return ans
    }
}
