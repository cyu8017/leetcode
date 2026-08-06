// LeetCode 1105 - Filling Bookcase Shelves
// https://leetcode.com/problems/filling-bookcase-shelves/

object Solution {
  def minHeightShelves(books: Array[Array[Int]], shelfWidth: Int): Int = {
    val n = books.length
    val dp = Array.fill(n + 1)(0)
    for (i <- 1 to n) {
      var width = 0
      var height = 0
      dp(i) = Int.MaxValue
      var j = i
      while (j >= 1) {
        val w = books(j - 1)(0)
        val h = books(j - 1)(1)
        width += w
        if (width > shelfWidth) {
          j = 0
        } else {
          height = math.max(height, h)
          dp(i) = math.min(dp(i), dp(j - 1) + height)
          j -= 1
        }
      }
    }
    dp(n)
  }
}
