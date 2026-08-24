// LeetCode 0805 - Split Array With Same Average
// https://leetcode.com/problems/split-array-with-same-average/

object Solution {
  def splitArraySameAverage(nums: Array[Int]): Boolean = {
    val n = nums.length
    val total = nums.sum
    scala.util.Sorting.quickSort(nums)
    val memo = scala.collection.mutable.Set.empty[Long]
    def find(target: Int, count: Int, index: Int): Boolean = {
      if (count == 0) return target == 0
      if (index == n || count + index > n || target < 0) return false
      val key = (target.toLong << 20) | (count.toLong << 10) | index
      if (memo.contains(key)) return false
      if (find(target - nums(index), count - 1, index + 1) || find(target, count, index + 1)) return true
      memo += key
      false
    }
    var size = 1
    while (size < n) {
      if ((total * size) % n == 0 && find(total * size / n, size, 0)) return true
      size += 1
    }
    false
  }
}
