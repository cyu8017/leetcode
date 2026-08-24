// LeetCode 0791 - Custom Sort String
// https://leetcode.com/problems/custom-sort-string/

object Solution {
  def customSortString(order: String, s: String): String = {
    val count = Array.ofDim[Int](26)
    s.foreach(ch => count(ch - 'a') += 1)
    val sb = new StringBuilder
    order.foreach { ch =>
      while (count(ch - 'a') > 0) {
        sb.append(ch)
        count(ch - 'a') -= 1
      }
    }
    var i = 0
    while (i < 26) {
      while (count(i) > 0) {
        sb.append(('a' + i).toChar)
        count(i) -= 1
      }
      i += 1
    }
    sb.toString
  }
}
