// LeetCode 2201 - Count Artifacts That Can Be Extracted
// https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

object Solution {
  def digArtifacts(n: Int, artifacts: Array[Array[Int]], dig: Array[Array[Int]]): Int = {
    val dug = scala.collection.mutable.HashSet.empty[Long]
    for (d <- dig) dug += ((d(0).toLong << 32) | (d(1).toLong & 0xffffffffL))
    var ans = 0
    for (a <- artifacts) {
      var ok = true
      var r = a(0)
      while (r <= a(2) && ok) {
        var c = a(1)
        while (c <= a(3) && ok) {
          if (!dug.contains((r.toLong << 32) | (c.toLong & 0xffffffffL))) ok = false
          c += 1
        }
        r += 1
      }
      if (ok) ans += 1
    }
    ans
  }
}
