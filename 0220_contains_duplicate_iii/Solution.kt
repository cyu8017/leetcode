// LeetCode 0220 - Contains Duplicate III
// https://leetcode.com/problems/contains-duplicate-iii/

class Solution {
    fun containsNearbyAlmostDuplicate(nums: IntArray, indexDiff: Int, valueDiff: Int): Boolean {
        if (indexDiff <= 0 || valueDiff < 0) {
            return false
        }
        val width = valueDiff.toLong() + 1
        val buckets = mutableMapOf<Long, Long>()

        fun bucketId(num: Long): Long {
            return if (num >= 0) num / width else (num + 1) / width - 1
        }

        for (i in nums.indices) {
            val num = nums[i].toLong()
            val bucket = bucketId(num)
            if (bucket in buckets) {
                return true
            }
            if (bucket - 1 in buckets && kotlin.math.abs(num - buckets[bucket - 1]!!) <= valueDiff) {
                return true
            }
            if (bucket + 1 in buckets && kotlin.math.abs(num - buckets[bucket + 1]!!) <= valueDiff) {
                return true
            }
            if (buckets.size >= indexDiff) {
                buckets.remove(bucketId(nums[i - indexDiff].toLong()))
            }
            buckets[bucket] = num
        }
        return false
    }
}
