// LeetCode 2804 - Array Prototype ForEach
// https://leetcode.com/problems/array-prototype-foreach/

trait ArrayCallback {
  def call(value: Int, index: Int, array: Array[Int]): Unit
}

object Solution {
  def forEach(arr: Array[Int], callback: ArrayCallback): Unit = {
    var i = 0
    while (i < arr.length) {
      callback.call(arr(i), i, arr)
      i += 1
    }
  }
}
