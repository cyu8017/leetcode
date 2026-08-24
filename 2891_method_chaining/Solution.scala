// LeetCode 2891 - Method Chaining
// https://leetcode.com/problems/method-chaining/

object Solution {
  def findHeavyAnimals(animals: Array[Any]): Array[Map[String, Any]] = {
    def weight(r: Any): Int = r match {
      case row: Seq[_] => row(3).asInstanceOf[Int]
      case row: Array[_] => row(3).asInstanceOf[Int]
      case row: Map[String, Any] @unchecked => row("weight").asInstanceOf[Int]
    }
    def name(r: Any): Any = r match {
      case row: Seq[_] => row(0)
      case row: Array[_] => row(0)
      case row: Map[String, Any] @unchecked => row("name")
    }
    animals.filter(weight(_) > 100).sortBy(r => -weight(r)).map(r => Map("name" -> name(r)))
  }
}
