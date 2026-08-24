// LeetCode 0656 - Coin Path
// https://leetcode.com/problems/coin-path/

class Solution {
    fun cheapestJump(coins: IntArray, maxJump: Int): List<Int> {
        val n = coins.size
        if (coins[n - 1] == -1) return emptyList()
        val inf = Long.MAX_VALUE / 4
        val cost = LongArray(n) { inf }
        val nxt = IntArray(n) { -1 }
        cost[n - 1] = coins[n - 1].toLong()
        for (i in n - 2 downTo 0) {
            if (coins[i] == -1) continue
            for (jump in 1..maxJump) {
                val j = i + jump
                if (j >= n) break
                if (cost[j] == inf) continue
                val candidate = coins[i].toLong() + cost[j]
                if (candidate < cost[i] || (candidate == cost[i] && (nxt[i] == -1 || j < nxt[i]))) {
                    cost[i] = candidate
                    nxt[i] = j
                }
            }
        }
        if (cost[0] == inf) return emptyList()
        val path = ArrayList<Int>()
        path.add(1)
        var i = 0
        while (i != n - 1) {
            i = nxt[i]
            path.add(i + 1)
        }
        return path
    }
}
