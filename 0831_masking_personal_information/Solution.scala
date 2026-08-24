// LeetCode 0831 - Masking Personal Information
// https://leetcode.com/problems/masking-personal-information/

object Solution {
  def maskPII(s: String): String = {
    var at = s.indexOf('@')
    if (at >= 0) {
      val lower = s.toLowerCase
      at = lower.indexOf('@')
      val name = lower.substring(0, at)
      val domain = lower.substring(at + 1)
      return name.charAt(0) + "*****" + name.charAt(name.length - 1) + "@" + domain
    }
    val digits = new StringBuilder
    s.foreach { ch => if (ch.isDigit) digits.append(ch) }
    val local = digits.substring(digits.length - 4)
    val country = digits.length - 10
    if (country == 0) "***-***-" + local
    else "+" + ("*" * country) + "-***-***-" + local
  }
}
