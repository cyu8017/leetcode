// LeetCode 2611 - Mice and Cheese
// https://leetcode.com/problems/mice-and-cheese/

object Solution {
  def miceAndCheese(reward1: Array[Int], reward2: Array[Int], k: Int): Int = {
    val n = reward1.length
    val diff = Array.fill(n)(0)
    var ans = 0
    var i = 0
    while (i < n) {
      ans += reward2(i)
      diff(i) = reward1(i) - reward2(i)
      i += 1
    }
    java.util.Arrays.sort(diff)
    i = 0
    while (i < k) {
      ans += diff(n - 1 - i)
      i += 1
    }
    ans
  }
}
