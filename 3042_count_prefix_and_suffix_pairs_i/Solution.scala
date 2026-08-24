// LeetCode 3042 - Count Prefix and Suffix Pairs I
// https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/

object Solution {
  def countPrefixSuffixPairs(words: Array[String]): Int = {
    var ans = 0
    var i = 0
    while (i < words.length) {
      val s = words(i)
      var j = i + 1
      while (j < words.length) {
        val t = words(j)
        if (t.length >= s.length && t.startsWith(s) && t.endsWith(s)) ans += 1
        j += 1
      }
      i += 1
    }
    ans
  }
}
