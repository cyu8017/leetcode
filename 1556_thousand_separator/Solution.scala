// LeetCode 1556 - Thousand Separator
// https://leetcode.com/problems/thousand-separator/

object Solution {
  def thousandSeparator(n: Int): String = {
    var s = n.toString
    val parts = scala.collection.mutable.ArrayBuffer.empty[String]
    while (s.nonEmpty) {
      parts += s.takeRight(3)
      s = s.dropRight(3)
    }
    parts.reverse.mkString(".")
  }
}
