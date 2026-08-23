// LeetCode 3413 - Maximum Coins From K Consecutive Bags
// https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

import java.util.Arrays;

class Solution {
    public long maximumCoins(int[][] coins, int k) {
        Arrays.sort(coins, (a, b) -> Integer.compare(a[0], b[0]));
        long ans = 0;
        int n = coins.length;
        for (int i = 0; i < n; i++) {
            long sum = 0;
            int start = coins[i][0];
            int end = start + k - 1;
            for (int j = i; j < n && coins[j][0] <= end; j++) {
                int l = coins[j][0];
                int r = coins[j][1];
                if (r > end) r = end;
                if (l < start) l = start;
                if (l <= r) sum += (long) (r - l + 1) * coins[j][2];
            }
            if (sum > ans) ans = sum;
        }
        for (int i = 0; i < n; i++) {
            long sum = 0;
            int end = coins[i][1];
            int start = end - k + 1;
            for (int j = 0; j <= i; j++) {
                int l = coins[j][0];
                int r = coins[j][1];
                if (l < start) l = start;
                if (r > end) r = end;
                if (l <= r) sum += (long) (r - l + 1) * coins[j][2];
            }
            if (sum > ans) ans = sum;
        }
        return ans;
    }
}
