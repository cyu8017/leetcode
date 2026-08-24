// LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
// https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

object Solution {
  def maxKDistinct(nums: Array[Int], k0: Int): Array[Int] = {
    java.util.Arrays.sort(nums)
    val n = nums.length
    val ans = new java.util.ArrayList[Integer]()
    var k = k0
    var i = n - 1
    var stop = false
    while (i >= 0 && !stop) {
      if (!(i + 1 < n && nums(i) == nums(i + 1))) {
        ans.add(nums(i))
        k -= 1
        if (k == 0) stop = true
      }
      i -= 1
    }
    val res = new Array[Int](ans.size())
    i = 0
    while (i < ans.size()) {
      res(i) = ans.get(i)
      i += 1
    }
    res
  }
}
