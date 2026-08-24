// LeetCode 2623 - Memoize
// https://leetcode.com/problems/memoize/

object Solution {
  def memoize(fn: Int => Int): Int => Int = {
    val cache = scala.collection.mutable.HashMap.empty[Int, Int]
    (x: Int) => {
      cache.get(x) match {
        case Some(v) => v
        case None =>
          val r = fn(x)
          cache(x) = r
          r
      }
    }
  }
}
