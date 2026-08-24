// LeetCode 2109 - Adding Spaces to a String
// https://leetcode.com/problems/adding-spaces-to-a-string/

object Solution {
  def addSpaces(s: String, spaces: Array[Int]): String = {
    val b = new StringBuilder(s.length + spaces.length)
    var j = 0
    var i = 0
    while (i < s.length) {
      if (j < spaces.length && spaces(j) == i) {
        b.append(' ')
        j += 1
      }
      b.append(s.charAt(i))
      i += 1
    }
    b.toString
  }
}
