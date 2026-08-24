// LeetCode 2103 - Rings and Rods
// https://leetcode.com/problems/rings-and-rods/

class Solution {
    fun countPoints(rings: String): Int {
        val mask = IntArray(10)
        var i = 0
        while (i < rings.length) {
            val c = rings[i]
            val r = rings[i + 1] - '0'
            val bit = when (c) {
                'R' -> 1
                'G' -> 2
                else -> 4
            }
            mask[r] = mask[r] or bit
            i += 2
        }
        var ans = 0
        for (m in mask) if (m == 7) ans++
        return ans
    }
}
