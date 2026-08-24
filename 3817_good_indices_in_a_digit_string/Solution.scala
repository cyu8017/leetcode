// LeetCode 3817 - Good Indices In A Digit String
// https://leetcode.com/problems/good-indices-in-a-digit-string/

object Solution {
  def goodIndices(s: String): Array[Int] = {
    val ans = new java.util.ArrayList[Integer]()
    var i = 0
    while (i < s.length) {
      val t = String.valueOf(i)
      val k = t.length
      if (i + 1 - k >= 0 && s.substring(i + 1 - k, k) == t) ans.add(i)
      i += 1
    }
    val out = new Array[Int](ans.size())
    i = 0
    while (i < out.length) {
      out(i) = ans.get(i)
      i += 1
    }
    out
  }
}
