// LeetCode 2404 - Most Frequent Even Element
// https://leetcode.com/problems/most-frequent-even-element/

object Solution {
  def mostFrequentEven(nums: Array[Int]): Int = {
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var ans = -1
    var best = 0
    nums.foreach { x =>
      if (x % 2 == 0) {
        val c = cnt.getOrElse(x, 0) + 1
        cnt(x) = c
        if (c > best || (c == best && (ans == -1 || x < ans))) {
          best = c
          ans = x
        }
      }
    }
    ans
  }
}
