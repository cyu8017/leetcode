// LeetCode 2886 - Change Data Type
// https://leetcode.com/problems/change-data-type/

object Solution {
  def changeDatatype(students: Array[Any]): Array[Any] = {
    students.map {
      case r: Seq[_] => Seq(r(0), r(1), r(2), r(3).toString.toInt)
      case r: Array[_] => Array(r(0), r(1), r(2), r(3).toString.toInt)
      case r: Map[String, Any] @unchecked =>
        r + ("grade" -> r("grade").toString.toInt)
    }
  }
}
