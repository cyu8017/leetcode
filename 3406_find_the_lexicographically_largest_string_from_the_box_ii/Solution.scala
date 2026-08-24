// LeetCode 3406 - Find the Lexicographically Largest String From the Box II
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-ii/

object Solution {
  def answerString(word: String, numFriends: Int): String = {
    if (numFriends == 1) return word
    val n = word.length
    val maxLen = n - (numFriends - 1)
    var ans = ""
    var i = 0
    while (i < n) {
      var end = i + maxLen
      if (end > n) end = n
      val cand = word.substring(i, end)
      if (cand.compareTo(ans) > 0) ans = cand
      i += 1
    }
    ans
  }
}
