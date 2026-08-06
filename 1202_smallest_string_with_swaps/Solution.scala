// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

object Solution {
  def smallestStringWithSwaps(s: String, pairs: List[List[Int]]): String = {
    val parent = Array.tabulate(s.length)(identity)
    def find(x: Int): Int = {
      var cur = x
      while (parent(cur) != cur) {
        parent(cur) = parent(parent(cur))
        cur = parent(cur)
      }
      cur
    }
    for (p <- pairs) parent(find(p(0))) = find(p(1))
    val groups = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ListBuffer[Char]]
    for (i <- s.indices) {
      groups.getOrElseUpdate(find(i), scala.collection.mutable.ListBuffer.empty) += s(i)
    }
    for (chars <- groups.values) {
      val sorted = chars.sorted(Ordering[Char].reverse)
      chars.clear()
      chars ++= sorted
    }
    val sb = new StringBuilder
    for (i <- s.indices) sb += groups(find(i)).remove(groups(find(i)).length - 1)
    sb.toString
  }
}
