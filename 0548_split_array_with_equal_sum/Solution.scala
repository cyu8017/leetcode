// LeetCode 0548 - Split Array with Equal Sum
// https://leetcode.com/problems/split-array-with-equal-sum/

import scala.collection.mutable

object Solution {
  def splitArray(nums: Array[Int]): Boolean = {
    val n = nums.length
    if (n < 7) {
      return false
    }

    val prefix = new Array[Int](n + 1)
    for (i <- nums.indices) {
      prefix(i + 1) = prefix(i) + nums(i)
    }

    for (j <- 3 until n - 3) {
      val seen = mutable.Set.empty[Int]
      for (i <- 1 until j - 1) {
        val first = prefix(i) - prefix(0)
        val second = prefix(j) - prefix(i + 1)
        if (first == second) {
          seen.add(first)
        }
      }

      for (k <- j + 2 until n - 1) {
        val third = prefix(k) - prefix(j + 1)
        val fourth = prefix(n) - prefix(k + 1)
        if (third == fourth && seen.contains(third)) {
          return true
        }
      }
    }

    false
  }
}
