// LeetCode 3676 - Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/

object Solution {
  def bowlSubarrays(nums: Array[Int]): Long = {
    val n = nums.length
    var ans = 0L
    val ngr = Array.fill(n)(-1)
    val ngl = Array.fill(n)(-1)
    val stack = new java.util.ArrayList[Integer]()
    var i = n - 1
    while (i >= 0) {
      while (!stack.isEmpty && nums(stack.get(stack.size() - 1)) < nums(i))
        stack.remove(stack.size() - 1)
      if (!stack.isEmpty) ngr(i) = stack.get(stack.size() - 1)
      stack.add(i)
      i -= 1
    }
    stack.clear()
    i = 0
    while (i < n) {
      while (!stack.isEmpty && nums(stack.get(stack.size() - 1)) < nums(i))
        stack.remove(stack.size() - 1)
      if (!stack.isEmpty) ngl(i) = stack.get(stack.size() - 1)
      stack.add(i)
      i += 1
    }
    i = 0
    while (i < n) {
      if (ngr(i) != -1 && ngr(i) - i >= 2) ans += 1
      if (ngl(i) != -1 && i - ngl(i) >= 2) ans += 1
      i += 1
    }
    ans
  }
}
