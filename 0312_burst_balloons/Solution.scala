// LeetCode 0312 - Burst Balloons

// https://leetcode.com/problems/burst-balloons/



object Solution {

  def maxCoins(nums: Array[Int]): Int = {

    val balloons = Array(1) ++ nums ++ Array(1)

    val size = balloons.length

    val dp = Array.fill(size, size)(0)

    for (length <- 3 to size) {

      for (left <- 0 to size - length) {

        val right = left + length - 1

        for (mid <- left + 1 until right) {

          val coins = dp(left)(mid) + dp(mid)(right) +

            balloons(left) * balloons(mid) * balloons(right)

          dp(left)(right) = math.max(dp(left)(right), coins)

        }

      }

    }

    dp(0)(size - 1)

  }

}

