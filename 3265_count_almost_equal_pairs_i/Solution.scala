// LeetCode 3265 - Count Almost Equal Pairs I
// https://leetcode.com/problems/count-almost-equal-pairs-i/

object Solution {
  def countPairs(nums: Array[Int]): Int = {
    var ans = 0
    var i = 0
    while (i < nums.length) {
      var j = i + 1
      while (j < nums.length) {
        if (almostEqual(nums(i), nums(j))) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }

  def sprintfNum(x0: Int): String = {
    if (x0 == 0) return "0"
    var x = x0
    val b = new StringBuilder
    while (x > 0) {
      b.insert(0, ('0' + x % 10).toChar)
      x /= 10
    }
    b.toString
  }

  def almostEqual(a: Int, b: Int): Boolean = {
    var sa = sprintfNum(a)
    var sb = sprintfNum(b)
    while (sa.length < sb.length) sa = "0" + sa
    while (sb.length < sa.length) sb = "0" + sb
    val diff = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < sa.length) {
      if (sa.charAt(i) != sb.charAt(i)) diff += i
      i += 1
    }
    if (diff.isEmpty) return true
    if (diff.length != 2) return false
    val i0 = diff(0)
    val j = diff(1)
    sa.charAt(i0) == sb.charAt(j) && sa.charAt(j) == sb.charAt(i0)
  }
}
