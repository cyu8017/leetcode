// LeetCode 2917 - Find the K-or of an Array
// https://leetcode.com/problems/find-the-k-or-of-an-array/

object Solution {
  def findKOr(nums: Array[Int], k: Int): Int = {
    var ans = 0
    for (b <- 0 until 31) {
      var cnt = 0
      nums.foreach { v => if ((v & (1 << b)) != 0) cnt += 1 }
      if (cnt >= k) ans |= 1 << b
    }
    ans
  }
}
