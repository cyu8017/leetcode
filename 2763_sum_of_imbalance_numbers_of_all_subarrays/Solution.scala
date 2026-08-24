// LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
// https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

object Solution {
  def sumImbalanceNumbers(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 0
    var i = 0
    while (i < n) {
      val seen = scala.collection.mutable.HashSet.empty[Int]
      val sortedVals = scala.collection.mutable.TreeSet.empty[Int]
      var imbalance = 0
      var j = i
      while (j < n) {
        val x = nums(j)
        if (!seen.contains(x)) {
          seen += x
          val nextOpt = sortedVals.rangeFrom(x).headOption
          val prevOpt = sortedVals.rangeTo(x).lastOption
          if (prevOpt.exists(x - _ != 1)) imbalance += 1
          if (nextOpt.exists(_ - x != 1)) imbalance += 1
          if (prevOpt.isDefined && nextOpt.isDefined && nextOpt.get - prevOpt.get > 1) imbalance -= 1
          sortedVals += x
        }
        ans += imbalance
        j += 1
      }
      i += 1
    }
    ans
  }
}
