// LeetCode 0668 - Kth Smallest Number in Multiplication Table
// https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

object Solution {
  def findKthNumber(m: Int, n: Int, k: Int): Int = {
    var lo = 1
    var hi = m * n
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (countLe(m, n, mid) >= k) hi = mid else lo = mid + 1
    }
    lo
  }

  private def countLe(m: Int, n: Int, x: Int): Int = {
    var count = 0
    var row = 1
    while (row <= m) {
      count += math.min(x / row, n)
      row += 1
    }
    count
  }
}
