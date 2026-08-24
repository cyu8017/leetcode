// LeetCode 2857 - Count Pairs of Points With Distance k
// https://leetcode.com/problems/count-pairs-of-points-with-distance-k/

class Solution {
    fun countPairs(coordinates: List<List<Int>>, k: Int): Int {
        val freq = HashMap<Long, Int>()
        var ans = 0
        for (p in coordinates) {
            val x = p[0]
            val y = p[1]
            for (a in 0..k) {
                val b = k - a
                ans += freq.getOrDefault(key(x xor a, y xor b), 0)
            }
            freq[key(x, y)] = freq.getOrDefault(key(x, y), 0) + 1
        }
        return ans
    }

    private fun key(x: Int, y: Int): Long {
        return (x.toLong() shl 32) xor (y.toLong() and 0xffffffffL)
    }
}
