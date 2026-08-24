// LeetCode 3874 - Valid Subarrays With Exactly One Peak
// https://leetcode.com/problems/valid-subarrays-with-exactly-one-peak/

object Solution {
  def validSubarrays(nums: Array[Int], k: Int): Long = {
    val n = nums.length
    val peaks = scala.collection.mutable.ArrayBuffer.empty[Int]
    var i = 1
    while (i < n - 1) {
      if (nums(i) > nums(i - 1) && nums(i) > nums(i + 1)) peaks += i
      i += 1
    }
    var ans = 0L
    var j = 0
    while (j < peaks.length) {
      val p = peaks(j)
      var leftMin = math.max(p - k, 0)
      if (j > 0) leftMin = math.max(leftMin, peaks(j - 1) + 1)
      var rightMax = math.min(p + k, n - 1)
      if (j < peaks.length - 1) rightMax = math.min(rightMax, peaks(j + 1) - 1)
      ans += (p - leftMin + 1).toLong * (rightMax - p + 1)
      j += 1
    }
    ans
  }
}
