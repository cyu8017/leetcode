// LeetCode 3113 - Find the Number of Subarrays Where Boundary Elements Are Maximum
// https://leetcode.com/problems/find-the-number-of-subarrays-where-boundary-elements-are-maximum/

object Solution {
  def numberOfSubarrays(nums: Array[Int]): Long = {
    val stk = new java.util.ArrayDeque[Array[Int]]()
    var ans = 0L
    nums.foreach { x =>
      while (!stk.isEmpty && stk.peekLast()(0) < x) stk.pollLast()
      if (stk.isEmpty || stk.peekLast()(0) > x) stk.addLast(Array(x, 1))
      else stk.peekLast()(1) += 1
      ans += stk.peekLast()(1)
    }
    ans
  }
}
