// LeetCode 2880 - Select Data
// https://leetcode.com/problems/select-data/

object Solution {
  def selectData(students: Array[Any]): Array[Map[String, Any]] = {
    students.flatMap {
      case r: Seq[_] if r.head == 101 => Some(Map("name" -> r(1), "age" -> r(2)))
      case r: Array[_] if r.head == 101 => Some(Map("name" -> r(1), "age" -> r(2)))
      case r: Map[String, Any] @unchecked if r.getOrElse("student_id", -1) == 101 =>
        Some(Map("name" -> r("name"), "age" -> r("age")))
      case _ => None
    }
  }
}
