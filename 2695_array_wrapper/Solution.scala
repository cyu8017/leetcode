// LeetCode 2695 - Array Wrapper
// https://leetcode.com/problems/array-wrapper/

class ArrayWrapper(private val nums: Array[Int]) {
  def valueOf(): Int = {
    var s = 0
    var i = 0
    while (i < nums.length) {
      s += nums(i)
      i += 1
    }
    s
  }

  override def toString: String = {
    val sb = new StringBuilder
    sb.append('[')
    var i = 0
    while (i < nums.length) {
      if (i > 0) sb.append(',')
      sb.append(nums(i))
      i += 1
    }
    sb.append(']')
    sb.toString
  }
}

object Solution {
  def arrayWrapperCreate(nums: Array[Int]): ArrayWrapper = new ArrayWrapper(nums)
}
