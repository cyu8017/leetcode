// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/

object Solution {
  def invertObject(obj: scala.collection.Map[String, String]): scala.collection.mutable.Map[String, List[String]] = {
    val output = scala.collection.mutable.LinkedHashMap.empty[String, List[String]]
    obj.foreach { case (k, v) =>
      output(v) = output.getOrElse(v, List.empty) :+ k
    }
    output
  }
}
