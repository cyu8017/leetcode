// LeetCode 1434 - Number of Ways to Wear Different Hats to Each Other
// https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

class Solution {
    fun numberWays(hats: List<List<Int>>): Int {
        val mod = 1_000_000_007
        val people = hats.size
        val wearers = Array(41) { mutableListOf<Int>() }
        for (person in hats.indices) {
            for (hat in hats[person]) {
                wearers[hat].add(person)
            }
        }
        var dp = IntArray(1 shl people)
        dp[0] = 1
        for (hat in 1..40) {
            val nxt = dp.copyOf()
            for (mask in dp.indices) {
                val ways = dp[mask]
                if (ways == 0) continue
                for (person in wearers[hat]) {
                    if (mask shr person and 1 == 0) {
                        val nextMask = mask or (1 shl person)
                        nxt[nextMask] = (nxt[nextMask] + ways) % mod
                    }
                }
            }
            dp = nxt
        }
        return dp[(1 shl people) - 1]
    }
}
