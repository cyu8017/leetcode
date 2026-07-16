// LeetCode 0480 - Sliding Window Median
// https://leetcode.com/problems/sliding-window-median/

import scala.collection.mutable

object Solution {
  private def bisectLeft(array: mutable.ArrayBuffer[Int], target: Int): Int = {
    var left = 0
    var right = array.length
    while (left < right) {
      val mid = left + (right - left) / 2
      if (array(mid) < target) left = mid + 1 else right = mid
    }
    left
  }

  private def insertSorted(array: mutable.ArrayBuffer[Int], value: Int): Unit = {
    val position = bisectLeft(array, value)
    array.insert(position, value)
  }

  def medianSlidingWindow(nums: Array[Int], k: Int): Array[Double] = {
    val window = mutable.ArrayBuffer.from(nums.take(k).sorted)
    val result = mutable.ArrayBuffer.empty[Double]

    def appendMedian(): Unit = {
      if (k % 2 == 1) {
        result += window(k / 2).toDouble
      } else {
        result += (window(k / 2 - 1) + window(k / 2)) / 2.0
      }
    }

    appendMedian()
    var index = k
    while (index < nums.length) {
      val outgoing = nums(index - k)
      val incoming = nums(index)
      window.remove(bisectLeft(window, outgoing))
      insertSorted(window, incoming)
      appendMedian()
      index += 1
    }
    result.toArray
  }
}
