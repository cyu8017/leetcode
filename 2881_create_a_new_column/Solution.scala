// LeetCode 2881 - Create a New Column
// https://leetcode.com/problems/create-a-new-column/

object Solution {
  def createBonusColumn(employees: Array[Any]): Array[Map[String, Any]] = {
    employees.map {
      case r: Seq[_] =>
        val salary = r(1).asInstanceOf[Int]
        Map("name" -> r(0), "salary" -> salary, "bonus" -> (salary * 2))
      case r: Array[_] =>
        val salary = r(1).asInstanceOf[Int]
        Map("name" -> r(0), "salary" -> salary, "bonus" -> (salary * 2))
      case r: Map[String, Any] @unchecked =>
        val salary = r("salary").asInstanceOf[Int]
        r + ("bonus" -> (salary * 2))
    }
  }
}
