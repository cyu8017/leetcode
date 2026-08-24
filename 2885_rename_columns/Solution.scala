// LeetCode 2885 - Rename Columns
// https://leetcode.com/problems/rename-columns/

object Solution {
  def renameColumns(students: Array[Any]): Array[Map[String, Any]] = {
    students.map {
      case r: Seq[_] =>
        Map("student_id" -> r(0), "first_name" -> r(1), "last_name" -> r(2), "age_in_years" -> r(3))
      case r: Array[_] =>
        Map("student_id" -> r(0), "first_name" -> r(1), "last_name" -> r(2), "age_in_years" -> r(3))
      case r: Map[String, Any] @unchecked =>
        Map(
          "student_id" -> r("id"),
          "first_name" -> r("first"),
          "last_name" -> r("last"),
          "age_in_years" -> r("age")
        )
    }
  }
}
