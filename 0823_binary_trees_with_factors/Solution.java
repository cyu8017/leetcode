// LeetCode 0823 - Binary Trees With Factors
// https://leetcode.com/problems/binary-trees-with-factors/

import java.util.*;

class Solution {
    public int numFactoredBinaryTrees(int[] arr) {
        final int MOD = 1_000_000_007;
        Arrays.sort(arr);
        Map<Integer, Long> dp = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            int x = arr[i];
            long ways = 1;
            for (int j = 0; j < i; j++) {
                int left = arr[j];
                if (x % left == 0) {
                    int right = x / left;
                    if (dp.containsKey(right)) {
                        ways = (ways + dp.get(left) * dp.get(right)) % MOD;
                    }
                }
            }
            dp.put(x, ways);
        }
        long ans = 0;
        for (long v : dp.values()) ans = (ans + v) % MOD;
        return (int) ans;
    }
}
