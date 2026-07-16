// LeetCode 0546 - Remove Boxes
// https://leetcode.com/problems/remove-boxes/

object Solution {
  def removeBoxes(boxes: Array[Int]): Int = {
    val n = boxes.length
    val memo = Array.fill(n, n, n)(-1)

    def dp(left: Int, right: Int, streak: Int): Int = {
      if (left > right) {
        return 0
      }
      if (memo(left)(right)(streak) != -1) {
        return memo(left)(right)(streak)
      }

      var r = right
      var s = streak
      while (r > left && boxes(r) == boxes(r - 1)) {
        r -= 1
        s += 1
      }

      var best = (s + 1) * (s + 1) + dp(left, r - 1, 0)
      for (i <- left until r if boxes(i) == boxes(r)) {
        best = math.max(best, dp(left, i, s + 1) + dp(i + 1, r - 1, 0))
      }

      memo(left)(right)(streak) = best
      best
    }

    dp(0, n - 1, 0)
  }
}
