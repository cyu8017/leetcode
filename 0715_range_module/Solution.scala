// LeetCode 0715 - Range Module
// https://leetcode.com/problems/range-module/

class RangeModule() {
  private var intervals = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]

  def addRange(left0: Int, right0: Int): Unit = {
    var left = left0
    var right = right0
    val next = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var placed = false
    for (iv <- intervals) {
      val start = iv(0)
      val end = iv(1)
      if (end < left) next += Array(start, end)
      else if (right < start) {
        if (!placed) {
          next += Array(left, right)
          placed = true
        }
        next += Array(start, end)
      } else {
        left = math.min(left, start)
        right = math.max(right, end)
      }
    }
    if (!placed) next += Array(left, right)
    intervals = next
  }

  def queryRange(left: Int, right: Int): Boolean = {
    for (iv <- intervals) {
      if (iv(0) <= left && right <= iv(1)) return true
      if (iv(1) >= right) return false
    }
    false
  }

  def removeRange(left: Int, right: Int): Unit = {
    val next = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    for (iv <- intervals) {
      val start = iv(0)
      val end = iv(1)
      if (end <= left || right <= start) next += Array(start, end)
      else {
        if (start < left) next += Array(start, left)
        if (right < end) next += Array(right, end)
      }
    }
    intervals = next
  }
}
