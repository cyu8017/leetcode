// LeetCode 2634 - Filter Elements from Array
// https://leetcode.com/problems/filter-elements-from-array/

object Solution {
  def filter(arr: Array[Int], fn: (Int, Int) => Boolean): Array[Int] = {
    val out = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < arr.length) {
      if (fn(arr(i), i)) out += arr(i)
      i += 1
    }
    out.toArray
  }
}
