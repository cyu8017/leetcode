// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

object Solution {
  def countGoodSubarrays(nums: Array[Int]): Long = {
    val n = nums.length
    val l = Array.fill(n)(-1)
    val stk = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < n) {
      val x = nums(i)
      while (stk.nonEmpty && nums(stk.last) < x && (nums(stk.last) | x) == x) {
        stk.remove(stk.length - 1)
      }
      if (stk.nonEmpty) l(i) = stk.last
      stk += i
      i += 1
    }
    val r = Array.fill(n)(n)
    stk.clear()
    i = n - 1
    while (i >= 0) {
      while (stk.nonEmpty && (nums(stk.last) | nums(i)) == nums(i)) {
        stk.remove(stk.length - 1)
      }
      if (stk.nonEmpty) r(i) = stk.last
      stk += i
      i -= 1
    }
    var ans = 0L
    i = 0
    while (i < n) {
      ans += (i - l(i)).toLong * (r(i) - i)
      i += 1
    }
    ans
  }
}
