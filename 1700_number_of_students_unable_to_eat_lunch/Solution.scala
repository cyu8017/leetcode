// LeetCode 1700 - Number of Students Unable to Eat Lunch
// https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/

object Solution {
  def countStudents(students: Array[Int], sandwiches: Array[Int]): Int = {
    val c = Array.fill(2)(0)
    for (x <- students) c(x) += 1
    for (i <- sandwiches.indices) {
      val x = sandwiches(i)
      if (c(x) == 0) return students.length - i
      c(x) -= 1
    }
    0
  }
}
