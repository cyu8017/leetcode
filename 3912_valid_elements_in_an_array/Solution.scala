// LeetCode 3912 - Valid Elements In An Array
// https://leetcode.com/problems/valid-elements-in-an-array/

object Solution {
  def findValidElements(nums: Array[Int]): Array[Int] = {
    val n = nums.length
    val right = new Array[Int](n)
    right(n - 1) = nums(n - 1)
    var i = n - 2
    while (i >= 0) {
      right(i) = math.max(right(i + 1), nums(i))
      i -= 1
    }
    var left = 0
    val ans = scala.collection.mutable.ArrayBuffer.empty[Int]
    i = 0
    while (i < n) {
      val x = nums(i)
      if (x > left || i == n - 1 || x > right(i + 1)) ans += x
      left = math.max(left, x)
      i += 1
    }
    ans.toArray
  }
}
