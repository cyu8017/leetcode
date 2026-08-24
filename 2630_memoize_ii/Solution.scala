// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/

object Solution {
  def memoizeII(fn: Array[Int] => Int): Array[Int] => Int = {
    val cache = scala.collection.mutable.HashMap.empty[String, Int]
    (args: Array[Int]) => {
      val sb = new StringBuilder
      var i = 0
      while (i < args.length) {
        sb.append('|')
        sb.append(args(i))
        i += 1
      }
      val k = sb.toString
      cache.get(k) match {
        case Some(v) => v
        case None =>
          val v = fn(args)
          cache(k) = v
          v
      }
    }
  }
}
