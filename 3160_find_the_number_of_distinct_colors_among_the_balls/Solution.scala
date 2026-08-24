// LeetCode 3160 - Find the Number of Distinct Colors Among the Balls
// https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/

object Solution {
  def queryResults(limit: Int, queries: Array[Array[Int]]): Array[Int] = {
    val g = scala.collection.mutable.Map.empty[Int, Int]
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    val ans = new Array[Int](queries.length)
    var ai = 0
    queries.foreach { q =>
      val x = q(0)
      val y = q(1)
      cnt(y) = cnt.getOrElse(y, 0) + 1
      g.get(x).foreach { old =>
        val nv = cnt(old) - 1
        if (nv == 0) cnt.remove(old)
        else cnt(old) = nv
      }
      g(x) = y
      ans(ai) = cnt.size
      ai += 1
    }
    ans
  }
}
