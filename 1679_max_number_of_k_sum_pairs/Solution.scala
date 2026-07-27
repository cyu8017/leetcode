// LeetCode 1679 - Max Number of K-Sum Pairs
// https://leetcode.com/problems/max-number-of-k-sum-pairs/

object Solution {
  def maxOperations(nums: Array[Int], k: Int): Int = {
    val c = scala.collection.mutable.Map.empty[Int, Int].withDefaultValue(0)
    var ans = 0
    for (x <- nums) {
      if (c(k - x) > 0) {
        c(k - x) -= 1
        ans += 1
      } else {
        c(x) += 1
      }
    }
    ans
  }
}
