// LeetCode 0266 - Palindrome Permutation
// https://leetcode.com/problems/palindrome-permutation/

object Solution {
  def canPermutePalindrome(s: String): Boolean = {
    val counts = Array.fill(26)(0)
    s.foreach { char =>
      counts(char - 'a') += 1
    }
    counts.count(_ % 2 != 0) <= 1
  }
}
