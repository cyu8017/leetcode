// LeetCode 0956 - Tallest Billboard
// https://leetcode.com/problems/tallest-billboard/

object Solution {
  def tallestBillboard(rods: Array[Int]): Int = {
    var dp = scala.collection.mutable.Map(0 -> 0)
    rods.foreach { rod =>
      val cur = dp.toList
      cur.foreach { case (diff, taller) =>
        val key1 = diff + rod
        dp(key1) = math.max(dp.getOrElse(key1, 0), taller + rod)
        val nd = math.abs(diff - rod)
        val nt = if (diff >= rod) taller else taller - diff + rod
        dp(nd) = math.max(dp.getOrElse(nd, 0), nt)
      }
    }
    dp.getOrElse(0, 0)
  }
}
