// LeetCode 1224 - Maximum Equal Frequency
// https://leetcode.com/problems/maximum-equal-frequency/

object Solution {
  def maxEqualFreq(nums: Array[Int]): Int = {
    val count = scala.collection.mutable.Map.empty[Int, Int].withDefaultValue(0)
    val frequencies = scala.collection.mutable.Map.empty[Int, Int].withDefaultValue(0)
    var answer = 0
    for (i <- 1 to nums.length) {
      val x = nums(i - 1)
      val old = count(x)
      if (old > 0) frequencies(old) -= 1
      count(x) = old + 1
      frequencies(old + 1) += 1
      val high = frequencies.keys.filter(frequencies(_) > 0).max
      if (high == 1 || frequencies(high) * high + 1 == i ||
          (frequencies(high) == 1 && frequencies(high - 1) * (high - 1) + high == i)) {
        answer = i
      }
    }
    answer
  }
}
