// LeetCode 2884 - Modify Columns
// https://leetcode.com/problems/modify-columns/

object Solution {
  def modifySalaryColumn(employees: Array[Any]): Array[Any] = {
    employees.map {
      case r: Seq[_] => Seq(r(0), r(1).asInstanceOf[Int] * 2)
      case r: Array[_] => Array(r(0), r(1).asInstanceOf[Int] * 2)
      case r: Map[String, Any] @unchecked =>
        r + ("salary" -> (r("salary").asInstanceOf[Int] * 2))
    }
  }
}
