// LeetCode 0416 - Partition Equal Subset Sum

// https://leetcode.com/problems/partition-equal-subset-sum/



object Solution {

  def canPartition(nums: Array[Int]): Boolean = {

    val total = nums.sum



    if (total % 2 != 0) {

      return false

    }



    val target = total / 2

    var possible = Set(0)



    for (value <- nums) {

      possible = possible ++ possible.flatMap { amount =>

        val sum = amount + value

        if (sum <= target) Some(sum) else None

      }



      if (possible.contains(target)) {

        return true

      }

    }



    possible.contains(target)

  }

}
