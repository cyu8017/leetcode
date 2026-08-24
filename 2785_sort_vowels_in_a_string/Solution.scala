// LeetCode 2785 - Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/

object Solution {
  def sortVowels(s: String): String = {
    def isVowel(c: Char): Boolean =
      c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
      c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'
    val vowels = s.filter(isVowel).sorted
    val arr = s.toCharArray
    var vi = 0
    var i = 0
    while (i < arr.length) {
      if (isVowel(arr(i))) {
        arr(i) = vowels(vi)
        vi += 1
      }
      i += 1
    }
    new String(arr)
  }
}
