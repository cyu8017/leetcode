// LeetCode 4007 - Widest Possible Fence
// https://leetcode.com/problems/widest-possible-fence/

import scala.collection.mutable

object Solution {
  def maximumWidth(planks: Array[Int]): Int = {
    val cnt = mutable.HashMap.empty[Int, Int]
    for (x <- planks) cnt(x) = cnt.getOrElse(x, 0) + 1
    val t = mutable.HashMap.empty[Int, Int]
    var ans = 0
    for ((x, v1) <- cnt) {
      t(x) = t.getOrElse(x, 0) + v1
      ans = math.max(ans, t(x))
      t(x * 2) = t.getOrElse(x * 2, 0) + v1 / 2
      ans = math.max(ans, t(x * 2))
      for ((y, v2) <- cnt) {
        if (y > x) {
          val key = x + y
          t(key) = t.getOrElse(key, 0) + math.min(v1, v2)
          ans = math.max(ans, t(key))
        }
      }
    }
    ans
  }
}
