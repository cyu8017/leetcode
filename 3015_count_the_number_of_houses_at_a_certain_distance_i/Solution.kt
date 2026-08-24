// LeetCode 3015 - Count the Number of Houses at a Certain Distance I
// https://leetcode.com/problems/count-the-number-of-houses-at-a-certain-distance-i/

class Solution {
    fun countOfPairs(n: Int, x: Int, y: Int): IntArray {
        var ans = IntArray(n)
        x--; y--
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                var a = j - i
                var b = kotlin.math.abs(x - i) + kotlin.math.abs(y - j) + 1
                var c = kotlin.math.abs(x - j) + kotlin.math.abs(y - i) + 1
                ans[minOf(a, minOf(b, c)) - 1] += 2
            }
        }
        return ans
    }
}
