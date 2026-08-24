// LeetCode 3648 - Minimum Sensors to Cover Grid
// https://leetcode.com/problems/minimum-sensors-to-cover-grid/

object Solution {
  def minSensors(n: Int, m: Int, k: Int): Int = {
    val cover = 2 * k + 1
    ((n + cover - 1) / cover) * ((m + cover - 1) / cover)
  }
}
