// LeetCode 2582 - Pass the Pillow
// https://leetcode.com/problems/pass-the-pillow/

object Solution {
  def passThePillow(n: Int, time: Int): Int = {
    val cycle = 2 * (n - 1)
    val t = time % cycle
    if (t < n) 1 + t
    else n - (t - (n - 1))
  }
}
