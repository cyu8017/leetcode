// LeetCode 0526 - Beautiful Arrangement
// https://leetcode.com/problems/beautiful-arrangement/

import scala.collection.mutable

object Solution {
  def countArrangement(n: Int): Int = backtrack(1, n, mutable.Set.empty[Int])

  private def backtrack(index: Int, n: Int, used: mutable.Set[Int]): Int = {
    if (index == n + 1) {
      return 1
    }
    var count = 0
    for (num <- 1 to n if !used.contains(num)) {
      if (index % num == 0 || num % index == 0) {
        used.add(num)
        count += backtrack(index + 1, n, used)
        used.remove(num)
      }
    }
    count
  }
}
