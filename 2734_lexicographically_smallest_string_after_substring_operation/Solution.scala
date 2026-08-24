// LeetCode 2734 - Lexicographically Smallest String After Substring Operation
// https://leetcode.com/problems/lexicographically-smallest-string-after-substring-operation/

object Solution {
  def smallestString(s: String): String = {
    val arr = s.toCharArray
    val n = arr.length
    var i = 0
    while (i < n && arr(i) == 'a') i += 1
    if (i == n) {
      arr(n - 1) = 'z'
      return new String(arr)
    }
    while (i < n && arr(i) != 'a') {
      arr(i) = (arr(i) - 1).toChar
      i += 1
    }
    new String(arr)
  }
}
