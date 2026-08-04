// LeetCode 1105 - Filling Bookcase Shelves
// https://leetcode.com/problems/filling-bookcase-shelves/

class Solution {
    fun minHeightShelves(books: Array<IntArray>, shelfWidth: Int): Int {
        val n = books.size
        val dp = IntArray(n + 1)
        for (i in 1..n) {
            var width = 0
            var height = 0
            dp[i] = Int.MAX_VALUE
            for (j in i downTo 1) {
                val w = books[j - 1][0]
                val h = books[j - 1][1]
                width += w
                if (width > shelfWidth) break
                height = maxOf(height, h)
                dp[i] = minOf(dp[i], dp[j - 1] + height)
            }
        }
        return dp[n]
    }
}
