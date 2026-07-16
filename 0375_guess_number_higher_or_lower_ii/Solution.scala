// LeetCode 0375 - Guess Number Higher or Lower II

// https://leetcode.com/problems/guess-number-higher-or-lower-ii/



object Solution {

  def getMoneyAmount(n: Int): Int = {

    val dp = Array.fill(n + 2, n + 2)(0)



    for (length <- 2 to n) {

      for (left <- 1 to n - length + 1) {

        val right = left + length - 1

        dp(left)(right) = Int.MaxValue

        for (guess <- left until right) {

          val cost = guess + math.max(dp(left)(guess - 1), dp(guess + 1)(right))

          dp(left)(right) = math.min(dp(left)(right), cost)

        }

      }

    }



    dp(1)(n)

  }

}
