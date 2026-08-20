// LeetCode 1248 - Count Number of Nice Subarrays
// https://leetcode.com/problems/count-number-of-nice-subarrays/

object Solution {
  def numberOfSubarrays(nums: Array[Int], k: Int): Int = {
    val frequency = scala.collection.mutable.Map(0 -> 1).withDefaultValue(0)
    var odd = 0
    var answer = 0
    for (x <- nums) {
      odd += x & 1
      answer += frequency(odd - k)
      frequency(odd) += 1
    }
    answer
  }
}
