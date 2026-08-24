// LeetCode 3221 - Maximum Array Hopping Score II
// https://leetcode.com/problems/maximum-array-hopping-score-ii/

object Solution {
  def maxScore(nums: Array[Int]): Long = {
    val stk = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < nums.length) {
      while (stk.nonEmpty && nums(stk.last) <= nums(i)) stk.remove(stk.length - 1)
      stk += i
      i += 1
    }
    var ans = 0L
    var cur = 0
    for (j <- stk) {
      ans += (j - cur).toLong * nums(j)
      cur = j
    }
    ans
  }
}
