// LeetCode 2882 - Drop Duplicate Rows
// https://leetcode.com/problems/drop-duplicate-rows/

object Solution {
  def dropDuplicateEmails(customers: Array[Any]): Array[Any] = {
    val seen = scala.collection.mutable.Set.empty[Any]
    customers.filter { r =>
      val email = r match {
        case row: Seq[_] => row(2)
        case row: Array[_] => row(2)
        case row: Map[String, Any] @unchecked => row("email")
      }
      if (seen.contains(email)) false
      else {
        seen += email
        true
      }
    }
  }
}
