// LeetCode 3026 - Maximum Good Subarray Sum
// https://leetcode.com/problems/maximum-good-subarray-sum/

object Solution {
  def maximumSubarraySum(nums: Array[Int], k: Int): Long = {
    val p = scala.collection.mutable.HashMap[Int, Long]()
    p(nums(0)) = 0L
    var s = 0L
    val n = nums.length
    var ans = Long.MinValue
    var i = 0
    while (i < n) {
      s += nums(i)
      if (p.contains(nums(i) - k)) ans = math.max(ans, s - p(nums(i) - k))
      if (p.contains(nums(i) + k)) ans = math.max(ans, s - p(nums(i) + k))
      if (i + 1 < n) {
        val old = p.get(nums(i + 1))
        if (old.isEmpty || s < old.get) p(nums(i + 1)) = s
      }
      i += 1
    }
    if (ans == Long.MinValue) 0 else ans
  }
}
