// LeetCode 2355 - Maximum Number of Books You Can Take
// https://leetcode.com/problems/maximum-number-of-books-you-can-take/

object Solution {
  def maximumBooks(books: Array[Int]): Long = {
    val n = books.length
    val dp = Array.fill(n)(0L)
    val stack = scala.collection.mutable.ArrayDeque.empty[Int]
    var ans = 0L
    var i = 0
    while (i < n) {
      while (stack.nonEmpty && books(stack.last) >= books(i) - (i - stack.last)) {
        stack.removeLast()
      }
      if (stack.isEmpty) dp(i) = sum(0, i, books(i))
      else {
        val j = stack.last
        dp(i) = dp(j) + sum(j + 1, i, books(i))
      }
      ans = math.max(ans, dp(i))
      stack.append(i)
      i += 1
    }
    ans
  }

  private def sum(l: Int, r: Int, h: Int): Long = {
    val width = r - l + 1
    if (h >= width) width.toLong * (2L * h - width + 1) / 2
    else h.toLong * (h + 1) / 2
  }
}
