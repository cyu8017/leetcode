// LeetCode 2171 - Removing Minimum Number of Magic Beans
// https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

object Solution {
  def minimumRemoval(beans: Array[Int]): Long = {
    val sorted = beans.sorted
    val n = sorted.length
    var sum = 0L
    sorted.foreach(b => sum += b)
    var ans = sum
    var i = 0
    while (i < n) {
      val remain = 1L * (n - i) * sorted(i)
      ans = math.min(ans, sum - remain)
      i += 1
    }
    ans
  }
}
