// LeetCode 0324 - Wiggle Sort II

// https://leetcode.com/problems/wiggle-sort-ii/



object Solution {

  def wiggleSort(nums: Array[Int]): Unit = {

    val sortedNums = nums.sorted

    var left = (nums.length - 1) / 2

    var right = nums.length - 1

    for (index <- nums.indices) {

      if (index % 2 == 0) {

        nums(index) = sortedNums(left)

        left -= 1

      } else {

        nums(index) = sortedNums(right)

        right -= 1

      }

    }

  }

}

