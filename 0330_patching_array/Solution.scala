// LeetCode 0330 - Patching Array

// https://leetcode.com/problems/patching-array/



object Solution {

  def minPatches(nums: Array[Int], n: Int): Int = {

    var patches = 0

    var miss = 1L

    var index = 0

    while (miss <= n) {

      if (index < nums.length && nums(index) <= miss) {

        miss += nums(index)

        index += 1

      } else {

        miss += miss

        patches += 1

      }

    }

    patches

  }

}

