// LeetCode 0954 - Array of Doubled Pairs
// https://leetcode.com/problems/array-of-doubled-pairs/

object Solution {
  def canReorderDoubled(arr: Array[Int]): Boolean = {
    val count = scala.collection.mutable.Map.empty[Int, Int]
    arr.foreach { x => count(x) = count.getOrElse(x, 0) + 1 }
    val keys = count.keys.toList.sortBy(math.abs)
    keys.foreach { x =>
      val need = count(x)
      if (need != 0) {
        if (count.getOrElse(2 * x, 0) < need) return false
        count(2 * x) = count(2 * x) - need
      }
    }
    true
  }
}
