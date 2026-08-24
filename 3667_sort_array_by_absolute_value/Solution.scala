// LeetCode 3667 - Sort Array By Absolute Value
// https://leetcode.com/problems/sort-array-by-absolute-value/

object Solution {
  def sortByAbsoluteValue(nums: Array[Int]): Array[Int] = {
    val boxed = new Array[Integer](nums.length)
    var i = 0
    while (i < nums.length) {
      boxed(i) = nums(i)
      i += 1
    }
    java.util.Arrays.sort(boxed, (a: Integer, b: Integer) => Integer.compare(math.abs(a), math.abs(b)))
    i = 0
    while (i < nums.length) {
      nums(i) = boxed(i)
      i += 1
    }
    nums
  }
}
