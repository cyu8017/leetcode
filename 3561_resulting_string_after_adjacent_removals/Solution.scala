// LeetCode 3561 - Resulting String After Adjacent Removals
// https://leetcode.com/problems/resulting-string-after-adjacent-removals/

object Solution {
  def isContiguous(a: Char, b: Char): Boolean = {
    val x = math.abs(a - b)
    x == 1 || x == 25
  }

  def resultingString(s: String): String = {
    val stk = new StringBuilder
    for (c <- s.toCharArray) {
      if (stk.length > 0 && isContiguous(stk.charAt(stk.length - 1), c))
        stk.deleteCharAt(stk.length - 1)
      else stk.append(c)
    }
    stk.toString
  }
}
