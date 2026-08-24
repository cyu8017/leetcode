// LeetCode 2663 - Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

object Solution {
  def smallestBeautifulString(s: String, k: Int): String = {
    val n = s.length
    val b = s.toCharArray
    var i = n - 1
    while (i >= 0) {
      var c = (b(i) + 1).toChar
      while (c < ('a' + k).toChar) {
        if (!((i > 0 && c == b(i - 1)) || (i > 1 && c == b(i - 2)))) {
          b(i) = c
          var j = i + 1
          while (j < n) {
            var nc = 'a'
            var placed = false
            while (nc < ('a' + k).toChar && !placed) {
              if (!((j > 0 && nc == b(j - 1)) || (j > 1 && nc == b(j - 2)))) {
                b(j) = nc
                placed = true
              }
              nc = (nc + 1).toChar
            }
            j += 1
          }
          return new String(b)
        }
        c = (c + 1).toChar
      }
      i -= 1
    }
    ""
  }
}
