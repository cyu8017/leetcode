// LeetCode 0325 - Maximum Size Subarray Sum Equals k

// https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/



import scala.collection.mutable



object Solution {

  def maxSubArrayLen(nums: Array[Int], k: Int): Int = {

    val prefixIndex = mutable.Map(0 -> -1)

    var prefix = 0

    var best = 0

    for ((index, num) <- nums.zipWithIndex) {

      prefix += num

      prefixIndex.get(prefix - k).foreach { start =>

        best = math.max(best, index - start)

      }

      if (!prefixIndex.contains(prefix)) {

        prefixIndex(prefix) = index

      }

    }

    best

  }

}

