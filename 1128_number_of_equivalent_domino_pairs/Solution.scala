// LeetCode 1128 - Number of Equivalent Domino Pairs
// https://leetcode.com/problems/number-of-equivalent-domino-pairs/

object Solution {
  def numEquivDominoPairs(dominoes: Array[Array[Int]]): Int = {
    val count = scala.collection.mutable.Map.empty[Int, Int]
    var ans = 0
    for (d <- dominoes) {
      val a = math.min(d(0), d(1))
      val b = math.max(d(0), d(1))
      val key = a * 10 + b
      ans += count.getOrElse(key, 0)
      count(key) = count.getOrElse(key, 0) + 1
    }
    ans
  }
}
