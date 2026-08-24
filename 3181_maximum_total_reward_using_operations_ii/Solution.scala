// LeetCode 3181 - Maximum Total Reward Using Operations II
// https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

object Solution {
  def maxTotalReward(rewardValues: Array[Int]): Int = {
    java.util.Arrays.sort(rewardValues)
    var uniq = 0
    var i = 0
    while (i < rewardValues.length) {
      if (uniq == 0 || rewardValues(i) != rewardValues(uniq - 1)) {
        rewardValues(uniq) = rewardValues(i)
        uniq += 1
      }
      i += 1
    }
    var f = java.math.BigInteger.ONE
    i = 0
    while (i < uniq) {
      val v = rewardValues(i)
      val mask = f.and(java.math.BigInteger.ONE.shiftLeft(v).subtract(java.math.BigInteger.ONE))
      f = f.or(mask.shiftLeft(v))
      i += 1
    }
    i = 100000
    while (i >= 0) {
      if (f.testBit(i)) return i
      i -= 1
    }
    0
  }
}
