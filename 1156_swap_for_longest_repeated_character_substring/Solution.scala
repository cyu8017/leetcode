// LeetCode 1156 - Swap For Longest Repeated Character Substring
// https://leetcode.com/problems/swap-for-longest-repeated-character-substring/

object Solution {
  def maxRepOpt1(text: String): Int = {
    val count = text.groupBy(identity).view.mapValues(_.length).toMap
    val n = text.length
    var ans = 0
    var i = 0
    while (i < n) {
      var j = i
      while (j < n && text(j) == text(i)) j += 1
      val length = j - i
      var k = j + 1
      while (k < n && text(k) == text(i)) k += 1
      val length2 = if (j < n) k - j - 1 else 0
      ans = math.max(ans, math.min(length + length2 + 1, count(text(i))))
      i = j
    }
    ans
  }
}
