// LeetCode 3861 - Minimum Capacity Box
// https://leetcode.com/problems/minimum-capacity-box/

object Solution {
  def minimumIndex(capacity: Array[Int], itemSize: Int): Int = {
    var ans = -1
    var i = 0
    while (i < capacity.length) {
      if (capacity(i) >= itemSize && (ans == -1 || capacity(i) < capacity(ans))) ans = i
      i += 1
    }
    ans
  }
}
