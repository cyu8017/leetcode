// LeetCode 0698 - Partition to K Equal Sum Subsets
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

object Solution {
  def canPartitionKSubsets(nums: Array[Int], k: Int): Boolean = {
    var total = 0
    for (x <- nums) total += x
    if (total % k != 0) return false
    val target = total / k
    val arr = nums.clone()
    scala.util.Sorting.quickSort(arr)
    var i = 0
    var j = arr.length - 1
    while (i < j) {
      val tmp = arr(i)
      arr(i) = arr(j)
      arr(j) = tmp
      i += 1
      j -= 1
    }
    if (arr(0) > target) return false
    val buckets = Array.fill(k)(0)
    def dfs(index: Int): Boolean = {
      if (index == arr.length) return true
      var b = 0
      while (b < buckets.length) {
        if (buckets(b) + arr(index) <= target) {
          buckets(b) += arr(index)
          if (dfs(index + 1)) return true
          buckets(b) -= arr(index)
          if (buckets(b) == 0) return false
        }
        b += 1
      }
      false
    }
    dfs(0)
  }
}
