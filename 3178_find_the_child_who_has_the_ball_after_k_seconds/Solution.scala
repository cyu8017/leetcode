// LeetCode 3178 - Find the Child Who Has the Ball After K Seconds
// https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/

object Solution {
  def numberOfChild(n: Int, k: Int): Int = {
    val mod = k % (n - 1)
    val rounds = k / (n - 1)
    if (rounds % 2 == 1) n - mod - 1 else mod
  }
}
