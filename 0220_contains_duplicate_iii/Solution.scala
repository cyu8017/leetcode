// LeetCode 0220 - Contains Duplicate III
// https://leetcode.com/problems/contains-duplicate-iii/

import scala.collection.mutable

object Solution {
  def containsNearbyAlmostDuplicate(nums: Array[Int], indexDiff: Int, valueDiff: Int): Boolean = {
    if (indexDiff <= 0 || valueDiff < 0) {
      return false
    }
    val width = valueDiff.toLong + 1
    val buckets = mutable.Map.empty[Long, Long]

    def bucketId(num: Long): Long =
      if (num >= 0) num / width else (num + 1) / width - 1

    for (i <- nums.indices) {
      val num = nums(i).toLong
      val bucket = bucketId(num)
      if (buckets.contains(bucket)) {
        return true
      }
      if (buckets.get(bucket - 1).exists(prev => math.abs(num - prev) <= valueDiff)) {
        return true
      }
      if (buckets.get(bucket + 1).exists(prev => math.abs(num - prev) <= valueDiff)) {
        return true
      }
      if (buckets.size >= indexDiff) {
        buckets.remove(bucketId(nums(i - indexDiff).toLong))
      }
      buckets(bucket) = num
    }
    false
  }
}
