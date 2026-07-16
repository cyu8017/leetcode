// LeetCode 0396 - Rotate Function

// https://leetcode.com/problems/rotate-function/



object Solution {

  def maxRotateFunction(nums: Array[Int]): Int = {

    val total = nums.sum

    var current = nums.indices.map(index => index * nums(index)).sum

    var best = current



    for (index <- nums.length - 1 to 1 by -1) {

      current += total - nums.length * nums(index)

      best = math.max(best, current)

    }



    best

  }

}
