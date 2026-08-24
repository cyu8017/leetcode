// LeetCode 2621 - Sleep
// https://leetcode.com/problems/sleep/

object Solution {
  def sleep(millis: Int): Unit = {
    Thread.sleep(millis.toLong)
  }
}
