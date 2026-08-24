// LeetCode 2798 - Number of Employees Who Met the Target
// https://leetcode.com/problems/number-of-employees-who-met-the-target/

object Solution {
  def numberOfEmployeesWhoMetTarget(hours: Array[Int], target: Int): Int =
    hours.count(_ >= target)
}
