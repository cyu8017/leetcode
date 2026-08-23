// LeetCode 3413 - Maximum Coins From K Consecutive Bags
// https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long maximumCoins(std::vector<std::vector<int>>& coins, int k) {
        std::sort(coins.begin(), coins.end(), [](auto& a, auto& b) { return a[0] < b[0]; });
        long long ans = 0;
        int n = (int)coins.size();
        for (int i = 0; i < n; i++) {
            long long sum = 0;
            int start = coins[i][0];
            int end = start + k - 1;
            for (int j = i; j < n && coins[j][0] <= end; j++) {
                int l = coins[j][0];
                int r = coins[j][1];
                if (r > end) r = end;
                if (l < start) l = start;
                if (l <= r) sum += (long long)(r - l + 1) * coins[j][2];
            }
            if (sum > ans) ans = sum;
        }
        for (int i = 0; i < n; i++) {
            long long sum = 0;
            int end = coins[i][1];
            int start = end - k + 1;
            for (int j = 0; j <= i; j++) {
                int l = coins[j][0];
                int r = coins[j][1];
                if (l < start) l = start;
                if (r > end) r = end;
                if (l <= r) sum += (long long)(r - l + 1) * coins[j][2];
            }
            if (sum > ans) ans = sum;
        }
        return ans;
    }
};
