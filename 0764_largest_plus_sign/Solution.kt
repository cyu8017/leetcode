// LeetCode 0764 - Largest Plus Sign
// https://leetcode.com/problems/largest-plus-sign/

class Solution {
    fun orderOfLargestPlusSign(n: Int, mines: Array<IntArray>): Int {
        var banned = HashSet<Int>()
        for (mine in mines) { banned.add(mine[0] * n + mine[1]) }
        var arms = Array(n) { IntArray(n) }
        var best = 0
        for (r in 0 until n) {
            var count = 0
            for (c in 0 until n) {
                count = if (banned.contains(r * n + c)) 0 else count + 1
                arms[r][c] = count
            }
            count = 0
            for (c in n - 1 downTo 0) {
                count = if (banned.contains(r * n + c)) 0 else count + 1
                arms[r][c] = minOf(arms[r][c], count)
            }
        }
        for (c in 0 until n) {
            var count = 0
            for (r in 0 until n) {
                count = if (banned.contains(r * n + c)) 0 else count + 1
                arms[r][c] = minOf(arms[r][c], count)
            }
            count = 0
            for (r in n - 1 downTo 0) {
                count = if (banned.contains(r * n + c)) 0 else count + 1
                arms[r][c] = minOf(arms[r][c], count)
                best = maxOf(best, arms[r][c])
            }
        }
        return best
    }
}
