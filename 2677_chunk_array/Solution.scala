// LeetCode 2677 - Chunk Array
// https://leetcode.com/problems/chunk-array/

object Solution {
  def chunk(arr: Array[Int], size: Int): Array[Array[Int]] = {
    val ans = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    var i = 0
    while (i < arr.length) {
      val end = math.min(arr.length, i + size)
      ans += arr.slice(i, end)
      i += size
    }
    ans.toArray
  }
}
