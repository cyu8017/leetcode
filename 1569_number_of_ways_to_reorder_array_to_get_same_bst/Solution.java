// LeetCode 1569 - Number of Ways to Reorder Array to Get Same BST
// https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;
    private int[][] choose;

    public int numOfWays(int[] nums) {
        int n = nums.length;
        choose = new int[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            choose[i][0] = 1;
            choose[i][i] = 1;
            for (int j = 1; j < i; j++) {
                choose[i][j] = (choose[i - 1][j - 1] + choose[i - 1][j]) % MOD;
            }
        }
        return (ways(nums) - 1 + MOD) % MOD;
    }

    private int ways(int[] values) {
        if (values.length < 3) {
            return 1;
        }
        List<Integer> left = new ArrayList<>();
        List<Integer> right = new ArrayList<>();
        for (int i = 1; i < values.length; i++) {
            if (values[i] < values[0]) {
                left.add(values[i]);
            } else {
                right.add(values[i]);
            }
        }
        int[] leftArr = left.stream().mapToInt(Integer::intValue).toArray();
        int[] rightArr = right.stream().mapToInt(Integer::intValue).toArray();
        long result = choose[values.length - 1][left.size()];
        result = result * ways(leftArr) % MOD;
        result = result * ways(rightArr) % MOD;
        return (int) result;
    }
}
