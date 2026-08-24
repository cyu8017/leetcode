// LeetCode 0702 - Search in a Sorted Array of Unknown Size
// https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/

class ArrayReader(secret: Array[Int]) {
  def get(index: Int): Int = {
    if (index < 0 || index >= secret.length) 2147483647 else secret(index)
  }
}

object Solution {
  def search(secret: Array[Int], target: Int): Int = search(new ArrayReader(secret), target)

  def search(reader: ArrayReader, target: Int): Int = {
    var right = 1
    while (reader.get(right) < target) right <<= 1
    var left = right >> 1
    while (left <= right) {
      val mid = left + (right - left) / 2
      val value = reader.get(mid)
      if (value == target) return mid
      if (value > target) right = mid - 1
      else left = mid + 1
    }
    -1
  }
}
