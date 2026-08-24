// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/

object Solution {
  def once(fn: Int => Int): Int => Option[Int] = {
    var called = false
    var res = 0
    (arg: Int) => {
      if (called) None
      else {
        called = true
        res = fn(arg)
        Some(res)
      }
    }
  }
}
