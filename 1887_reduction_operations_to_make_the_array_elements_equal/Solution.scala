// LeetCode 1887 - Reduction Operations to Make the Array Elements Equal
// https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/

object Solution {
  def reductionOperations(nums: Array[Int]): Int = {
    val sorted = nums.sorted
    var answer = 0
    var rank = 0
    for (i <- 1 until sorted.length) {
      if (sorted(i) != sorted(i - 1)) rank += 1
      answer += rank
    }
    answer
  }
}
