// LeetCode 1521 - Find a Value of a Mysterious Function Closest to Target
// https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/

object Solution {
  def closestToTarget(arr: Array[Int], target: Int): Int = {
    var answer = Int.MaxValue
    var current = Set.empty[Int]
    for (value <- arr) {
      current = Set(value) ++ current.map(_ & value)
      answer = math.min(answer, current.map(c => math.abs(c - target)).min)
    }
    answer
  }
}
