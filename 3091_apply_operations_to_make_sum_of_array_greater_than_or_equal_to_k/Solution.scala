// LeetCode 3091 - Apply Operations to Make Sum of Array Greater Than or Equal to k
// https://leetcode.com/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/

object Solution {
  def minOperations(k: Int): Int = {
    var ans = k
    var a = 0
    while (a < k) {
      val x = a + 1
      val b = (k + x - 1) / x - 1
      ans = math.min(ans, a + b)
      a += 1
    }
    ans
  }
}
