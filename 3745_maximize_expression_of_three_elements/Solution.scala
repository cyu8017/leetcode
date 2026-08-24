// LeetCode 3745 - Maximize Expression of Three Elements
// https://leetcode.com/problems/maximize-expression-of-three-elements/

object Solution {
  def maximizeExpressionOfThree(nums: Array[Int]): Int = {
    val inf = 1 << 30
    var a = -inf
    var b = -inf
    var c = inf
    nums.foreach { x =>
      if (x < c) c = x
      if (x >= a) { b = a; a = x }
      else if (x > b) b = x
    }
    a + b - c
  }
}
