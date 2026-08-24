// LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

object Solution {
  def minOperations(nums: Array[Int]): Int = {
    val stk = new java.util.ArrayList[Integer]()
    var ans = 0
    for (x <- nums) {
      while (stk.size() > 0 && stk.get(stk.size() - 1) > x) {
        ans += 1
        stk.remove(stk.size() - 1)
      }
      if (x != 0 && (stk.size() == 0 || stk.get(stk.size() - 1) != x)) stk.add(x)
    }
    ans += stk.size()
    ans
  }
}
