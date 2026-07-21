// LeetCode 1817 - Finding the Users Active Minutes
// https://leetcode.com/problems/finding-the-users-active-minutes/

object Solution {
  def findingUsersActiveMinutes(logs: Array[Array[Int]], k: Int): Array[Int] = {
    val userMinutes = scala.collection.mutable.Map.empty[Int, scala.collection.mutable.Set[Int]]
    for (log <- logs) {
      val userId = log(0)
      val minute = log(1)
      userMinutes.getOrElseUpdate(userId, scala.collection.mutable.Set.empty[Int]) += minute
    }
    val answer = Array.fill(k)(0)
    for (minutes <- userMinutes.values) {
      val uam = minutes.size
      if (uam <= k) answer(uam - 1) += 1
    }
    answer
  }
}
