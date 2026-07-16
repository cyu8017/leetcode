// LeetCode 0486 - Predict the Winner
// https://leetcode.com/problems/predict-the-winner/

object Solution {
  def predictTheWinner(nums: Array[Int]): Boolean = {
    val n = nums.length
    val dp = Array.ofDim[Int](n, n)
    for (i <- 0 until n) dp(i)(i) = nums(i)
    for (length <- 2 to n; left <- 0 to n - length) {
      val right = left + length - 1
      dp(left)(right) = math.max(
        nums(left) - dp(left + 1)(right),
        nums(right) - dp(left)(right - 1),
      )
    }
    dp(0)(n - 1) >= 0
  }
}
