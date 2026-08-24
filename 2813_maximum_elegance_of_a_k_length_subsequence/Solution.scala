// LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

object Solution {
  def findMaximumElegance(items: Array[Array[Int]], k: Int): Long = {
    java.util.Arrays.sort(items, (a: Array[Int], b: Array[Int]) => Integer.compare(b(0), a(0)))
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var total = 0L
    val dup = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 0
    while (i < k) {
      total += items(i)(0)
      val c = items(i)(1)
      if (seen.contains(c)) dup += items(i)(0)
      else seen += c
      i += 1
    }
    var ans = total + seen.size.toLong * seen.size
    i = k
    while (i < items.length) {
      val c = items(i)(1)
      if (!seen.contains(c) && dup.nonEmpty) {
        total += items(i)(0) - dup.last
        dup.remove(dup.length - 1)
        seen += c
        ans = math.max(ans, total + seen.size.toLong * seen.size)
      }
      i += 1
    }
    ans
  }
}
