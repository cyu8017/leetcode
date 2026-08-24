// LeetCode 0917 - Reverse Only Letters
// https://leetcode.com/problems/reverse-only-letters/

object Solution {
  def reverseOnlyLetters(s: String): String = {
    val arr = s.toCharArray
    var i = 0
    var j = arr.length - 1
    while (i < j) {
      while (i < j && !arr(i).isLetter) i += 1
      while (i < j && !arr(j).isLetter) j -= 1
      val tmp = arr(i)
      arr(i) = arr(j)
      arr(j) = tmp
      i += 1
      j -= 1
    }
    new String(arr)
  }
}
