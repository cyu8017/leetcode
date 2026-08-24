// LeetCode 0929 - Unique Email Addresses
// https://leetcode.com/problems/unique-email-addresses/

object Solution {
  def numUniqueEmails(emails: Array[String]): Int = {
    val normalized = scala.collection.mutable.Set.empty[String]
    emails.foreach { email =>
      val at = email.indexOf('@')
      var local = email.substring(0, at)
      val domain = email.substring(at)
      val plus = local.indexOf('+')
      if (plus >= 0) local = local.substring(0, plus)
      val cleaned = new StringBuilder
      local.foreach { c => if (c != '.') cleaned.append(c) }
      normalized += cleaned.toString + domain
    }
    normalized.size
  }
}
