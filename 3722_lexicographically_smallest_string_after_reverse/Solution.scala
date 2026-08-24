// LeetCode 3722 - Lexicographically Smallest String After Reverse
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse/

object Solution {
  def lexSmallest(s: String): String = {
    var ans = s
    val n = s.length
    var k = 1
    while (k <= n) {
      val a1 = s.toCharArray
      reverse(a1, 0, 0 + k)
      val t1 = new String(a1)
      val a2 = s.toCharArray
      reverse(a2, n - k, n - k + k)
      val t2 = new String(a2)
      if (t1.compareTo(ans) < 0) ans = t1
      if (t2.compareTo(ans) < 0) ans = t2
      k += 1
    }
    ans
  }

  private def reverse(a: Array[Char], l: Int, r: Int): Unit = {
    var i = l
    var j = r - 1
    while (i < j) {
      val t = a(i); a(i) = a(j); a(j) = t
      i += 1
      j -= 1
    }
  }
}
