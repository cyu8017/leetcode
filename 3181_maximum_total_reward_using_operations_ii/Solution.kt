// LeetCode 3181 - Maximum Total Reward Using Operations II
// https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

import java.math.BigInteger

class Solution {
    fun maxTotalReward(rewardValues: IntArray): Int {
        rewardValues.sort()
        var uniq = 0
        for (i in rewardValues.indices) {
            if (uniq == 0 || rewardValues[i] != rewardValues[uniq - 1]) {
                rewardValues[uniq++] = rewardValues[i]
            }
        }
        var f = BigInteger.ONE
        for (i in 0 until uniq) {
            val v = rewardValues[i]
            val mask = f.and(BigInteger.ONE.shiftLeft(v).subtract(BigInteger.ONE))
            f = f.or(mask.shiftLeft(v))
        }
        for (i in 100000 downTo 0) {
            if (f.testBit(i)) return i
        }
        return 0
    }
}
