// LeetCode 1894 - Find the Student that Will Replace the Chalk
// https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/

object Solution {
  def chalkReplacer(chalk: Array[Int], k: Int): Int = {
    var remaining = k.toLong % chalk.map(_.toLong).sum
    for (index <- chalk.indices) {
      if (remaining < chalk(index)) return index
      remaining -= chalk(index)
    }
    0
  }
}
