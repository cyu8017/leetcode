// LeetCode 2185 - Counting Words With a Given Prefix
// https://leetcode.com/problems/counting-words-with-a-given-prefix/

object Solution {
  def prefixCount(words: Array[String], pref: String): Int = {
    words.count(w => w.length >= pref.length && w.startsWith(pref))
  }
}
