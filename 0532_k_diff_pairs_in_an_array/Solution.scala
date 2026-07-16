// LeetCode 0532 - K-diff Pairs in an Array
// https://leetcode.com/problems/k-diff-pairs-in-an-array/

object Solution {
  def findPairs(nums: Array[Int], k: Int): Int = {
    if (k < 0) {
      return 0
    }

    val freq = nums.groupBy(identity).view.mapValues(_.length)
    freq.keys.count { num =>
      if (k == 0) freq(num) > 1 else freq.contains(num + k)
    }
  }
}
