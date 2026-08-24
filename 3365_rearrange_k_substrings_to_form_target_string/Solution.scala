// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

object Solution {
  def isPossibleToRearrange(s: String, t: String, k: Int): Boolean = {
    val n = s.length
    val sz = n / k
    val cnt = scala.collection.mutable.HashMap.empty[String, Int]
    var i = 0
    while (i < n) {
      val a = s.substring(i, i + sz)
      val b = t.substring(i, i + sz)
      cnt(a) = cnt.getOrElse(a, 0) + 1
      cnt(b) = cnt.getOrElse(b, 0) - 1
      i += sz
    }
    cnt.values.forall(_ == 0)
  }
}
