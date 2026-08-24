// LeetCode 2883 - Drop Missing Data
// https://leetcode.com/problems/drop-missing-data/

object Solution {
  def dropMissingData(students: Array[Any]): Array[Any] = {
    students.filter { r =>
      val name = r match {
        case row: Seq[_] => row(1)
        case row: Array[_] => row(1)
        case row: Map[String, Any] @unchecked => row.getOrElse("name", null)
      }
      name != null && name != ""
    }
  }
}
