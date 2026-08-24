// LeetCode 2877 - Create a DataFrame from List
// https://leetcode.com/problems/create-a-dataframe-from-list/

object Solution {
  def createDataframe(student_data: Array[Array[Int]]): Array[Map[String, Int]] = {
    student_data.map { row =>
      Map("student_id" -> row(0), "age" -> row(1))
    }
  }
}
