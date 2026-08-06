// LeetCode 1980 - Find Unique Binary String
// https://leetcode.com/problems/find-unique-binary-string/

object Solution {
  def findDifferentBinaryString(nums: Array[String]): String = {
    val s = nums.toSet
    val n = nums.length
    for (i <- 0 until (1 << n)) {
      val cand = i.toBinaryString.reverse.padTo(n, '0').reverse.mkString
      if (!s.contains(cand)) return cand
    }
    "0" * n
  }
}
