// LeetCode 0413 - Arithmetic Slices

// https://leetcode.com/problems/arithmetic-slices/



object Solution {

  def numberOfArithmeticSlices(nums: Array[Int]): Int = {

    if (nums.length < 3) {

      return 0

    }



    var total = 0

    var current = 0



    for (index <- 2 until nums.length) {

      if (nums(index) - nums(index - 1) == nums(index - 1) - nums(index - 2)) {

        current += 1

        total += current

      } else {

        current = 0

      }

    }



    total

  }

}
