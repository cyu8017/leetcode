// LeetCode 2351 - First Letter to Appear Twice
// https://leetcode.com/problems/first-letter-to-appear-twice/

object Solution {
  def repeatedCharacter(s: String): Char = {
    val seen = Array.fill(26)(false)
    s.foreach { c =>
      val i = c - 'a'
      if (seen(i)) return c
      seen(i) = true
    }
    0.toChar
  }
}
