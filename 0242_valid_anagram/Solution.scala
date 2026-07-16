// LeetCode 0242 - Valid Anagram
// https://leetcode.com/problems/valid-anagram/

object Solution {
  def isAnagram(s: String, t: String): Boolean = {
    if (s.length != t.length) {
      false
    } else {
      val counts = Array.fill(26)(0)
      s.indices.foreach { index =>
        counts(s(index) - 'a') += 1
        counts(t(index) - 'a') -= 1
      }
      counts.forall(_ == 0)
    }
  }
}
