// LeetCode 2562 - Find the Array Concatenation Value
// https://leetcode.com/problems/find-the-array-concatenation-value/

object Solution {
  def findTheArrayConcVal(nums: Array[Int]): Long = {
    var ans = 0L
    var l = 0
    var r = nums.length - 1
    while (l <= r) {
      if (l == r) {
        ans += nums(l)
        return ans
      }
      val left = nums(l)
      val right = nums(r)
      var pow = 1L
      var t = right
      while (t > 0) {
        pow *= 10
        t /= 10
      }
      ans += left.toLong * pow + right
      l += 1
      r -= 1
    }
    ans
  }
}
