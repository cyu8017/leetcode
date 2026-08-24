// LeetCode 3189 - Minimum Moves to Get a Peaceful Board
// https://leetcode.com/problems/minimum-moves-to-get-a-peaceful-board/

class Solution {
    fun minMoves(rooks: Array<IntArray>): Int {
        var ans = 0
        rooks.sortWith { a, b -> a[0].compareTo(b[0]) }
        for (i in rooks.indices) ans += kotlin.math.abs(rooks[i][0] - i)
        rooks.sortWith { a, b -> a[1].compareTo(b[1]) }
        for (j in rooks.indices) ans += kotlin.math.abs(rooks[j][1] - j)
        return ans
    }
}
