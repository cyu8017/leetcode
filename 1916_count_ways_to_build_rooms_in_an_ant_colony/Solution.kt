// LeetCode 1916 - Count Ways To Build Rooms In An Ant Colony
// https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

class Solution {
    fun waysToBuildRooms(prevRoom: IntArray): Int {
        val mod = 1_000_000_007L
        val n = prevRoom.size
        val children = Array(n) { mutableListOf<Int>() }
        for (room in 1 until n) children[prevRoom[room]].add(room)

        val fact = LongArray(n + 1)
        val invFact = LongArray(n + 1)
        fact[0] = 1
        for (i in 1..n) fact[i] = fact[i - 1] * i % mod
        invFact[n] = modPow(fact[n], mod - 2, mod)
        for (i in n downTo 1) invFact[i - 1] = invFact[i] * i % mod

        fun comb(a: Int, b: Int): Long = fact[a] * invFact[b] % mod * invFact[a - b] % mod

        fun dfs(node: Int): Pair<Int, Long> {
            var size = 0
            var ways = 1L
            for (child in children[node]) {
                val (childSize, childWays) = dfs(child)
                ways = ways * childWays % mod * comb(size + childSize, childSize) % mod
                size += childSize
            }
            return size + 1 to ways
        }
        return dfs(0).second.toInt()
    }

    private fun modPow(base: Long, exp: Long, mod: Long): Long {
        var b = base % mod
        var e = exp
        var res = 1L
        while (e > 0) {
            if (e and 1L == 1L) res = res * b % mod
            b = b * b % mod
            e = e shr 1
        }
        return res
    }
}
