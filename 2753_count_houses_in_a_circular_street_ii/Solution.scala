// LeetCode 2753 - Count Houses in a Circular Street II
// https://leetcode.com/problems/count-houses-in-a-circular-street-ii/

object Solution {
  def houseCount(street: Array[Int], k: Int): Int = {
    val n = street.length
    if (n == 0) return 0
    var start = -1
    var i = 0
    while (i < n && start < 0) {
      if (street(i) == 1) start = i
      i += 1
    }
    if (start < 0) return 0
    var count = 1
    var moves = 0
    var i2 = start
    while (moves < k) {
      i2 = (i2 + 1) % n
      moves += 1
      if (i2 == start) return count
      if (street(i2) == 1) count += 1
    }
    count
  }
}
