// LeetCode 2244 - Minimum Rounds to Complete All Tasks
// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

object Solution {
  def minimumRounds(tasks: Array[Int]): Int = {
    val freq = scala.collection.mutable.HashMap.empty[Int, Int]
    for (t <- tasks) freq(t) = freq.getOrElse(t, 0) + 1
    var ans = 0
    for (c <- freq.values) {
      if (c == 1) return -1
      ans += (c + 2) / 3
    }
    ans
  }
}
