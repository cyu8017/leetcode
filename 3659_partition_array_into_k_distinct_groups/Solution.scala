// LeetCode 3659 - Partition Array Into K-Distinct Groups
// https://leetcode.com/problems/partition-array-into-k-distinct-groups/

object Solution {
  def partitionArray(nums: Array[Int], k: Int): Boolean = {
    val n = nums.length
    if (n % k != 0) return false
    val m = n / k
    var mx = 0
    for (x <- nums) mx = math.max(mx, x)
    val cnt = new Array[Int](mx + 1)
    for (x <- nums) {
      cnt(x) += 1
      if (cnt(x) > m) return false
    }
    true
  }
}
