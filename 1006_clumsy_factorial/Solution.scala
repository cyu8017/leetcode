// LeetCode 1006 - Clumsy Factorial
// https://leetcode.com/problems/clumsy-factorial/

object Solution {
  def clumsy(n: Int): Int = {
    val stack = scala.collection.mutable.ArrayBuffer(n)
    var cur = n - 1
    var op = 0
    while (cur > 0) {
      op % 4 match {
        case 0 => stack(stack.length - 1) = stack.last * cur
        case 1 => stack(stack.length - 1) = stack.last / cur
        case 2 => stack += cur
        case _ => stack += -cur
      }
      cur -= 1
      op += 1
    }
    stack.sum
  }
}
