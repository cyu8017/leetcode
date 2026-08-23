// LeetCode 3181 - Maximum Total Reward Using Operations II
// https://leetcode.com/problems/maximum-total-reward-using-operations-ii/

using System;
using System.Numerics;

public class Solution {
    public int MaxTotalReward(int[] rewardValues) {
        Array.Sort(rewardValues);
        int uniq = 0;
        for (int i = 0; i < rewardValues.Length; i++) {
            if (uniq == 0 || rewardValues[i] != rewardValues[uniq - 1])
                rewardValues[uniq++] = rewardValues[i];
        }
        BigInteger f = BigInteger.One;
        for (int i = 0; i < uniq; i++) {
            int v = rewardValues[i];
            BigInteger mask = f & ((BigInteger.One << v) - 1);
            f |= mask << v;
        }
        for (int i = 100000; i >= 0; i--) {
            if (!((f & (BigInteger.One << i)).IsZero)) return i;
        }
        return 0;
    }
}
