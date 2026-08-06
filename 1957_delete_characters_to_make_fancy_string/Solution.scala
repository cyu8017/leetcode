// LeetCode 1957 - Delete Characters to Make Fancy String
// https://leetcode.com/problems/delete-characters-to-make-fancy-string/

object Solution {
  def makeFancyString(s: String): String = {
    val ans = new StringBuilder
    for (c <- s) {
      if (!(ans.length >= 2 && ans.charAt(ans.length - 1) == c && ans.charAt(ans.length - 2) == c)) {
        ans.append(c)
      }
    }
    ans.toString
  }
}
