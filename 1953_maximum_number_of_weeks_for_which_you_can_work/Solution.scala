// LeetCode 1953 - Maximum Number of Weeks for Which You Can Work
// https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/

object Solution {
  def numberOfWeeks(milestones: Array[Int]): Long = {
    val total = milestones.map(_.toLong).sum
    val mx = milestones.max.toLong
    val rest = total - mx
    if (mx > rest + 1) 2 * rest + 1 else total
  }
}
