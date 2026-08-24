// LeetCode 3860 - Unique Email Groups
// https://leetcode.com/problems/unique-email-groups/

object Solution {
  def uniqueEmailGroups(emails: Array[String]): Int = {
    val st = scala.collection.mutable.Set.empty[String]
    emails.foreach { email =>
      val at = email.indexOf('@')
      var local = email.substring(0, at)
      val domain = email.substring(at + 1).toLowerCase
      val plus = local.indexOf('+')
      if (plus >= 0) local = local.substring(0, plus)
      val cleaned = new StringBuilder
      local.foreach { c => if (c != '.') cleaned.append(c.toLower) }
      st += cleaned.toString + domain
    }
    st.size
  }
}
