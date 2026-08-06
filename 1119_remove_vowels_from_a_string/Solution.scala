// LeetCode 1119 - Remove Vowels from a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

object Solution {
  def removeVowels(s: String): String =
    s.filter(ch => !"aeiou".contains(ch))
}
