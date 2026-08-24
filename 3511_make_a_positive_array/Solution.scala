// LeetCode 3511 - Make a Positive Array
// https://leetcode.com/problems/make-a-positive-array/

object Solution {
  def makeArrayPositive(nums: Array[Int]): Int = {
    var ans = 0
    var l = -1
    var preMx = 0L
    var s = 0L
    var r = 0
    while (r < nums.length) {
      s += nums(r)
      if (r - l > 2 && s <= preMx) {
        ans += 1
        l = r
        preMx = 0
        s = 0
      } else if (r - l >= 2) {
        preMx = math.max(preMx, s - nums(r) - nums(r - 1))
      }
      r += 1
    }
    ans
  }
}
