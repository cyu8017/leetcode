// LeetCode 3663 - Find The Least Frequent Digit
// https://leetcode.com/problems/find-the-least-frequent-digit/

object Solution {
  def getLeastFrequentDigit(n: Int): Int = {
    val cnt = new Array[Int](10)
    var ans = 0
    var f = 1 << 30
    var x = n
    while (x > 0) {
      cnt(x % 10) += 1
      x /= 10
    }
    var d = 0
    while (d < 10) {
      if (cnt(d) > 0 && cnt(d) < f) {
        f = cnt(d)
        ans = d
      }
      d += 1
    }
    ans
  }
}
