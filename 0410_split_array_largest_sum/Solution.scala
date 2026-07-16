// LeetCode 0410 - Split Array Largest Sum

// https://leetcode.com/problems/split-array-largest-sum/



object Solution {

  def splitArray(nums: Array[Int], k: Int): Int = {

    var left = nums.max

    var right = nums.sum



    while (left < right) {

      val mid = left + (right - left) / 2



      if (canSplit(nums, k, mid)) {

        right = mid

      } else {

        left = mid + 1

      }

    }



    left

  }



  private def canSplit(nums: Array[Int], k: Int, limit: Int): Boolean = {

    var parts = 1

    var current = 0



    for (value <- nums) {

      if (current + value > limit) {

        parts += 1

        current = 0

      }

      current += value

    }



    parts <= k

  }

}
