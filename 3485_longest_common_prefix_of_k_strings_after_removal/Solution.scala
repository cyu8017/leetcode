// LeetCode 3485 - Longest Common Prefix of K Strings After Removal
// https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal/

object Solution {
  private def lcpOf(a: java.util.List[String]): Int = {
    if (a.isEmpty) return 0
    var pref = a.get(0)
    var t = 1
    while (t < a.size()) {
      val s = a.get(t)
      var i = 0
      while (i < pref.length && i < s.length && pref.charAt(i) == s.charAt(i)) i += 1
      pref = pref.substring(0, i)
      if (pref.isEmpty) return 0
      t += 1
    }
    pref.length
  }

  def longestCommonPrefix(words: Array[String], k: Int): Array[Int] = {
    val n = words.length
    val ans = new Array[Int](n)
    var i = 0
    while (i < n) {
      val rest = new java.util.ArrayList[String]()
      var j = 0
      while (j < n) {
        if (j != i) rest.add(words(j))
        j += 1
      }
      if (rest.size() < k) ans(i) = 0
      else {
        java.util.Collections.sort(rest)
        var best = 0
        j = 0
        while (j + k - 1 < rest.size()) {
          val window = rest.subList(j, j + k)
          best = math.max(best, lcpOf(window))
          j += 1
        }
        ans(i) = best
      }
      i += 1
    }
    ans
  }
}
