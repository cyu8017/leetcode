// LeetCode 2963 - Count the Number of Good Partitions
// https://leetcode.com/problems/count-the-number-of-good-partitions/

object Solution {
  def numberOfGoodPartitions(nums: Array[Int]): Int = {
    val mod = 1000000007
    val last = scala.collection.mutable.HashMap[Int, Int]()
    var i = 0
    while (i < nums.length) { last(nums(i)) = i; i += 1 }
    var ans = 1
    var end = 0
    i = 0
    while (i < nums.length) {
      if (last(nums(i)) > end) end = last(nums(i))
      if (i == end && i != nums.length - 1) ans = ((ans * 2L) % mod).toInt
      i += 1
    }
    ans
  }
}
