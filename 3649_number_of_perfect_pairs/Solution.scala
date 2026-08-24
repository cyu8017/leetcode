// LeetCode 3649 - Number of Perfect Pairs
// https://leetcode.com/problems/number-of-perfect-pairs/

object Solution {
  def perfectPairs(nums: Array[Int]): Long = {
    val n = nums.length
    val absNums = new Array[Int](n)
    var i = 0
    while (i < n) {
      absNums(i) = math.abs(nums(i))
      i += 1
    }
    java.util.Arrays.sort(absNums)
    var ans = 0L
    var j = 0
    i = 0
    while (i < n) {
      if (j < i + 1) j = i + 1
      while (j < n && absNums(j) <= 2 * absNums(i)) j += 1
      ans += j - i - 1
      i += 1
    }
    ans
  }
}
