// LeetCode 1183 - Maximum Number of Ones
// https://leetcode.com/problems/maximum-number-of-ones/

class Solution {
    fun maximumNumberOfOnes(width: Int, height: Int, sideLength: Int, maxOnes: Int): Int {
        val counts = mutableListOf<Int>()
        for (r in 0 until sideLength) {
            for (c in 0 until sideLength) {
                val rows = (height - r + sideLength - 1) / sideLength
                val cols = (width - c + sideLength - 1) / sideLength
                counts.add(rows * cols)
            }
        }
        counts.sortDescending()
        var ans = 0
        for (i in 0 until minOf(maxOnes, counts.size)) ans += counts[i]
        return ans
    }
}
