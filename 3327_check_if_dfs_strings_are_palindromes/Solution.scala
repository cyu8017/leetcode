// LeetCode 3327 - Check DFS Strings Are Palindromes
// https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

object Solution {
  def findAnswer(parent: Array[Int], s: String): Array[Boolean] = {
    val n = parent.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    var i = 1
    while (i < n) {
      g(parent(i)) += i
      i += 1
    }
    val ans = new Array[Boolean](n)
    def isPal(t: String): Boolean = {
      var a = 0
      var b = t.length - 1
      while (a < b) {
        if (t.charAt(a) != t.charAt(b)) return false
        a += 1
        b -= 1
      }
      true
    }
    def dfsStr(u: Int): String = {
      val out = new StringBuilder
      for (v <- g(u)) out.append(dfsStr(v))
      out.append(s.charAt(u))
      ans(u) = isPal(out.toString)
      out.toString
    }
    dfsStr(0)
    ans
  }
}
