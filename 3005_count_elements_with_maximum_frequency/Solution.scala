// LeetCode 3005 - Count Elements With Maximum Frequency
// https://leetcode.com/problems/count-elements-with-maximum-frequency/

object Solution {
  def maxFrequencyElements(nums: Array[Int]): Int = {
    val cnt = Array.ofDim[Int](101)
    for (x <- nums) cnt(x) += 1
    var mx = -1
    var ans = 0
    for (x <- cnt) {
      if (mx < x) { mx = x; ans = x }
      else if (mx == x) ans += x
    }
    ans
  }
}
