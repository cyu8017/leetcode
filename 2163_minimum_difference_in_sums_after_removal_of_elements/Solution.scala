// LeetCode 2163 - Minimum Difference in Sums After Removal of Elements
// https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/

object Solution {
  def minimumDifference(nums: Array[Int]): Long = {
    val n = nums.length / 3
    val left = Array.fill(nums.length)(0L)
    val right = Array.fill(nums.length)(0L)
    val hmax = new java.util.PriorityQueue[Integer](java.util.Collections.reverseOrder())
    var sum = 0L
    var i = 0
    while (i < n) {
      hmax.offer(nums(i))
      sum += nums(i)
      i += 1
    }
    left(n - 1) = sum
    i = n
    while (i < 2 * n) {
      hmax.offer(nums(i))
      sum += nums(i)
      sum -= hmax.poll()
      left(i) = sum
      i += 1
    }
    val hmin = new java.util.PriorityQueue[Integer]()
    sum = 0
    i = nums.length - 1
    while (i >= 2 * n) {
      hmin.offer(nums(i))
      sum += nums(i)
      i -= 1
    }
    right(2 * n) = sum
    i = 2 * n - 1
    while (i >= n) {
      hmin.offer(nums(i))
      sum += nums(i)
      sum -= hmin.poll()
      right(i) = sum
      i -= 1
    }
    var ans = left(n - 1) - right(n)
    i = n
    while (i < 2 * n) {
      ans = math.min(ans, left(i) - right(i + 1))
      i += 1
    }
    ans
  }
}
