// LeetCode 0239 - Sliding Window Maximum
// https://leetcode.com/problems/sliding-window-maximum/

import scala.collection.mutable

object Solution {
  def maxSlidingWindow(nums: Array[Int], k: Int): Array[Int] = {
    val window = mutable.ArrayDeque.empty[Int]
    val result = mutable.ArrayBuffer.empty[Int]

    for (index <- nums.indices) {
      while (window.nonEmpty && nums(window.last) <= nums(index)) {
        window.removeLast()
      }
      window.append(index)
      if (window.head <= index - k) {
        window.removeHead()
      }
      if (index >= k - 1) {
        result.append(nums(window.head))
      }
    }

    result.toArray
  }
}
