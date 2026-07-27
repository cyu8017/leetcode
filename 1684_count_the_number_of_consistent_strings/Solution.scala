// LeetCode 1684 - Count the Number of Consistent Strings
// https://leetcode.com/problems/count-the-number-of-consistent-strings/

object Solution {
  def countConsistentStrings(allowed: String, words: Array[String]): Int = {
    val ok = Array.fill(26)(false)
    for (c <- allowed) ok(c - 'a') = true
    words.count(w => w.forall(c => ok(c - 'a')))
  }
}
