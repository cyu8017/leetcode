// LeetCode 0927 - Three Equal Parts
// https://leetcode.com/problems/three-equal-parts/

object Solution {
  def threeEqualParts(arr: Array[Int]): Array[Int] = {
    val ones = scala.collection.mutable.ArrayBuffer[Int]()
    var i = 0
    while (i < arr.length) {
      if (arr(i) != 0) ones += i
      i += 1
    }
    val n = ones.length
    if (n % 3 != 0) return Array(-1, -1)
    if (n == 0) return Array(0, arr.length - 1)
    val third = n / 3
    val length = ones.last - ones(2 * third) + 1
    val a = ones(0)
    val b = ones(third)
    val c = ones(2 * third)
    if (a + length > arr.length || b + length > arr.length || c + length > arr.length)
      return Array(-1, -1)
    i = 0
    while (i < length) {
      if (arr(a + i) != arr(b + i) || arr(a + i) != arr(c + i)) return Array(-1, -1)
      i += 1
    }
    Array(a + length - 1, b + length)
  }
}
