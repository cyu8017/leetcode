// LeetCode 3595 - Once Twice
// https://leetcode.com/problems/once-twice/

object Solution {
  def onceTwice(nums: Array[Int]): Array[Int] = {
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (x <- nums) freq(x) = freq.getOrElse(x, 0) + 1
    var a = 0
    var b = 0
    for ((k, v) <- freq) {
      if (v == 1) a = k
      else if (v == 2) b = k
    }
    Array(a, b)
  }
}
