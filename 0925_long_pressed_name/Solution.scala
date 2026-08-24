// LeetCode 0925 - Long Pressed Name
// https://leetcode.com/problems/long-pressed-name/

object Solution {
  def isLongPressedName(name: String, typed: String): Boolean = {
    var i = 0
    var j = 0
    while (j < typed.length) {
      if (i < name.length && name.charAt(i) == typed.charAt(j)) { i += 1; j += 1 }
      else if (j > 0 && typed.charAt(j) == typed.charAt(j - 1)) j += 1
      else return false
    }
    i == name.length
  }
}
