// LeetCode 3819 - Rotate Non Negative Elements
// https://leetcode.com/problems/rotate-non-negative-elements/

object Solution {
  def rotateElements(nums: Array[Int], k: Int): Array[Int] = {
    val t = new java.util.ArrayList[Integer]()
    nums.foreach(x => if (x >= 0) t.add(x))
    val m = t.size()
    if (m == 0) return nums
    val d = new Array[Int](m)
    var i = 0
    while (i < m) {
      d(((i - k) % m + m) % m) = t.get(i)
      i += 1
    }
    var j = 0
    i = 0
    while (i < nums.length) {
      if (nums(i) >= 0) {
        nums(i) = d(j)
        j += 1
      }
      i += 1
    }
    nums
  }
}
