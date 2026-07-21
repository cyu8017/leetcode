// LeetCode 1897 - Redistribute Characters to Make All Strings Equal
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

object Solution {
  def makeEqual(words: Array[String]): Boolean = {
    val counts = Array.fill(26)(0)
    for (word <- words; ch <- word) {
      counts(ch - 'a') += 1
    }
    val n = words.length
    counts.forall(_ % n == 0)
  }
}
