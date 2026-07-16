// LeetCode 0376 - Wiggle Subsequence

// https://leetcode.com/problems/wiggle-subsequence/



object Solution {

  def wiggleMaxLength(nums: Array[Int]): Int = {

    if (nums.length < 2) return nums.length



    var up = 1

    var down = 1



    for (index <- 1 until nums.length) {

      if (nums(index) > nums(index - 1)) {

        up = down + 1

      } else if (nums(index) < nums(index - 1)) {

        down = up + 1

      }

    }



    math.max(up, down)

  }

}
