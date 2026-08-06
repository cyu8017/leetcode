// LeetCode 1533 - Find the Index of the Large Integer
// https://leetcode.com/problems/find-the-index-of-the-large-integer/

trait ArrayReader {
  def compareSub(l: Int, r: Int, x: Int, y: Int): Int
  def length(): Int
}

object Solution {
  def getIndex(arr: Array[Int]): Int = {
    val reader = new ArrayReader {
      def compareSub(l: Int, r: Int, x: Int, y: Int): Int = {
        val a = arr.slice(l, r + 1).sum
        val b = arr.slice(x, y + 1).sum
        if (a > b) 1 else if (a < b) -1 else 0
      }
      def length(): Int = arr.length
    }
    getIndex(reader)
  }

  def getIndex(reader: ArrayReader): Int = {
    var left = 0
    var right = reader.length() - 1
    while (left < right) {
      val length = right - left + 1
      val half = length / 2
      val result = reader.compareSub(left, left + half - 1, right - half + 1, right)
      if (result == 0) return left + half
      if (result > 0) right = left + half - 1
      else left = right - half + 1
    }
    left
  }
}
