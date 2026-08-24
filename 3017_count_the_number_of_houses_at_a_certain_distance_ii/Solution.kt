// LeetCode 3017 - Count the Number of Houses at a Certain Distance II
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-ii/

class Solution {
    fun countOfPairs(n: Int, x0: Int, y0: Int): LongArray {
        var x = x0; var y = y0
        if (x > y) { val t = x; x = y; y = t }
        val A = LongArray(n)
        for (i in 1..n) {
            A[0] += 2
            A[minOf(i - 1, kotlin.math.abs(i - y) + x)] -= 1
            A[minOf(n - i, kotlin.math.abs(i - x) + 1 + (n - y))] -= 1
            A[minOf(kotlin.math.abs(i - x), kotlin.math.abs(y - i) + 1)] += 1
            A[minOf(kotlin.math.abs(i - x) + 1, kotlin.math.abs(y - i))] += 1
            val r = maxOf(x - i, 0) + maxOf(i - y, 0)
            A[r + (y - x) / 2] -= 1
            A[r + (y - x + 1) / 2] -= 1
        }
        for (i in 1 until n) A[i] += A[i - 1]
        return A
    }
}
