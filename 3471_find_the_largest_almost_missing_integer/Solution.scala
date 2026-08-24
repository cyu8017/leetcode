// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

object Solution {
  def largestInteger(nums: Array[Int], k: Int): Int = {
    val n = nums.length
    val cnt = scala.collection.mutable.Map.empty[Int, Int]
    var i = 0
    while (i + k <= n) {
      val seen = scala.collection.mutable.Set.empty[Int]
      var j = i
      while (j < i + k) { seen += nums(j); j += 1 }
      seen.foreach { x => cnt(x) = cnt.getOrElse(x, 0) + 1 }
      i += 1
    }
    var ans = -1
    cnt.foreach { case (key, value) =>
      if (value == 1 && key > ans) ans = key
    }
    ans
  }
}
