// LeetCode 3181 - Maximum Total Reward Using Operations II
// https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

import java.math.BigInteger;
import java.util.Arrays;

class Solution {
    public int maxTotalReward(int[] rewardValues) {
        Arrays.sort(rewardValues);
        int uniq = 0;
        for (int i = 0; i < rewardValues.length; i++) {
            if (uniq == 0 || rewardValues[i] != rewardValues[uniq - 1]) {
                rewardValues[uniq++] = rewardValues[i];
            }
        }
        BigInteger f = BigInteger.ONE;
        for (int i = 0; i < uniq; i++) {
            int v = rewardValues[i];
            BigInteger mask = f.and(BigInteger.ONE.shiftLeft(v).subtract(BigInteger.ONE));
            f = f.or(mask.shiftLeft(v));
        }
        for (int i = 100000; i >= 0; i--) {
            if (f.testBit(i)) {
                return i;
            }
        }
        return 0;
    }
}
