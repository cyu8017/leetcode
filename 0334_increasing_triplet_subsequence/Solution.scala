// LeetCode 0334 - Increasing Triplet Subsequence

// https://leetcode.com/problems/increasing-triplet-subsequence/



object Solution {

  def increasingTriplet(nums: Array[Int]): Boolean = {

    var first = Int.MaxValue

    var second = Int.MaxValue

    for (num <- nums) {

      if (num <= first) {

        first = num

      } else if (num <= second) {

        second = num

      } else {

        return true

      }

    }

    false

  }

}
