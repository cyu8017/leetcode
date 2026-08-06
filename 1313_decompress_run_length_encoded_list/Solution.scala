// LeetCode 1313 - Decompress Run-Length Encoded List
// https://leetcode.com/problems/decompress-run-length-encoded-list/

object Solution {
  def decompressRLElist(nums: Array[Int]): Array[Int] = {
    val answer = scala.collection.mutable.ArrayBuffer[Int]()
    var i = 0
    while (i < nums.length) {
      for (_ <- 0 until nums(i)) answer += nums(i + 1)
      i += 2
    }
    answer.toArray
  }
}
