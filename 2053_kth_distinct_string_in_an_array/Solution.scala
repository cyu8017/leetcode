// LeetCode 2053 - Kth Distinct String in an Array
// https://leetcode.com/problems/kth-distinct-string-in-an-array/

object Solution {
  def kthDistinct(arr: Array[String], k: Int): String = {
    val freq = scala.collection.mutable.Map.empty[String, Int]
    arr.foreach { s => freq(s) = freq.getOrElse(s, 0) + 1 }
    var kk = k
    arr.foreach { s =>
      if (freq(s) == 1) {
        kk -= 1
        if (kk == 0) return s
      }
    }
    ""
  }
}
