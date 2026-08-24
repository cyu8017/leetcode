// LeetCode 3201 - Find the Maximum Length of Valid Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/

object Solution {
  def maximumLength(nums: Array[Int]): Int = {
    val k = 2
    val f = Array.ofDim[Int](k, k)
    var ans = 0
    for (raw <- nums) {
      val x = raw % k
      var j = 0
      while (j < k) {
        val y = (j - x + k) % k
        f(x)(y) = f(y)(x) + 1
        ans = math.max(ans, f(x)(y))
        j += 1
      }
    }
    ans
  }
}
