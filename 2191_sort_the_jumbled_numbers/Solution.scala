// LeetCode 2191 - Sort the Jumbled Numbers
// https://leetcode.com/problems/sort-the-jumbled-numbers/

object Solution {
  private def mapVal(mapping: Array[Int], x0: Int): Int = {
    if (x0 == 0) return mapping(0)
    val digits = scala.collection.mutable.ArrayBuffer.empty[Int]
    var x = x0
    while (x > 0) {
      digits += x % 10
      x /= 10
    }
    var res = 0
    var i = digits.length - 1
    while (i >= 0) {
      res = res * 10 + mapping(digits(i))
      i -= 1
    }
    res
  }

  def sortJumbled(mapping: Array[Int], nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val arr = Array.tabulate(n)(i => (mapVal(mapping, nums(i)), i, nums(i)))
    arr.sortBy(t => (t._1, t._2)).map(_._3)
  }
}
