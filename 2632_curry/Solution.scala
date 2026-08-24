// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/

object Solution {
  def curry(fn: Array[Int] => Int, arity: Int): Array[Int] => Int = {
    (args: Array[Int]) => fn(args)
  }
}
