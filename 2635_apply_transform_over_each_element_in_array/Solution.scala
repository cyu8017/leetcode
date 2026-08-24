// LeetCode 2635 - Apply Transform Over Each Element in Array
// https://leetcode.com/problems/apply-transform-over-each-element-in-array/

object Solution {
  def map(arr: Array[Int], fn: (Int, Int) => Int): Array[Int] = {
    val out = new Array[Int](arr.length)
    var i = 0
    while (i < arr.length) {
      out(i) = fn(arr(i), i)
      i += 1
    }
    out
  }
}
