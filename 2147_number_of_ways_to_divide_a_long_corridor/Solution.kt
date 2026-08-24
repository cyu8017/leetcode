// LeetCode 2147 - Number of Ways to Divide a Long Corridor
// https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/

class Solution {
    fun numberOfWays(corridor: String): Int {
        val mod = 1_000_000_007
        val seats = mutableListOf<Int>()
        for (i in corridor.indices) if (corridor[i] == 'S') seats.add(i)
        if (seats.isEmpty() || seats.size % 2 != 0) return 0
        var ans = 1L
        var i = 2
        while (i < seats.size) {
            ans = ans * (seats[i] - seats[i - 1]) % mod
            i += 2
        }
        return ans.toInt()
    }
}
