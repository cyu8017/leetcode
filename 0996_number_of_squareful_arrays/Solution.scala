// LeetCode 0996 - Number of Squareful Arrays
// https://leetcode.com/problems/number-of-squareful-arrays/

object Solution {
  def numSquarefulPerms(nums: Array[Int]): Int = {
    val count = scala.collection.mutable.Map.empty[Int, Int]
    nums.foreach { x => count(x) = count.getOrElse(x, 0) + 1 }
    val graph = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    count.keys.foreach { a => graph(a) = scala.collection.mutable.ArrayBuffer.empty[Int] }
    for (a <- count.keys; b <- count.keys) {
      val s = a.toLong + b.toLong
      val r = math.round(math.sqrt(s.toDouble))
      if (r * r == s) graph(a) += b
    }
    var ans = 0
    def dfs(x: Int, remain: Int): Unit = {
      if (remain == 0) { ans += 1; return }
      graph(x).foreach { y =>
        if (count(y) > 0) {
          count(y) -= 1
          dfs(y, remain - 1)
          count(y) += 1
        }
      }
    }
    count.keys.toList.foreach { x =>
      count(x) -= 1
      dfs(x, nums.length - 1)
      count(x) += 1
    }
    ans
  }
}
