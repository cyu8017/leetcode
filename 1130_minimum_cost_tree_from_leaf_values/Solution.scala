// LeetCode 1130 - Minimum Cost Tree From Leaf Values
// https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

object Solution {
  def mctFromLeafValues(arr: Array[Int]): Int = {
    val stack = scala.collection.mutable.ArrayBuffer(Int.MaxValue)
    var ans = 0
    for (a <- arr) {
      while (stack.last <= a) {
        val mid = stack.remove(stack.length - 1)
        ans += mid * math.min(stack.last, a)
      }
      stack += a
    }
    while (stack.length > 2) {
      val mid = stack.remove(stack.length - 1)
      ans += mid * stack.last
    }
    ans
  }
}
