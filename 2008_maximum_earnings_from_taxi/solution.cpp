// LeetCode 2008 - Maximum Earnings From Taxi
// https://leetcode.com/problems/maximum-earnings-from-taxi/

#include <algorithm>
#include <array>
#include <bitset>
#include <cmath>
#include <cstdint>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

class Solution {
public:
    long long maxTaxiEarnings(int n, vector<vector<int>>& rides) {
        sort(rides.begin(), rides.end(), [](auto& a, auto& b) { return a[1] < b[1]; });
        int m = (int)rides.size();
        vector<int> ends(m);
        for (int i = 0; i < m; i++) ends[i] = rides[i][1];
        vector<long long> dp(m + 1);
        for (int i = 0; i < m; i++) {
            int start = rides[i][0], end = rides[i][1], tip = rides[i][2];
            long long earn = (long long)end - start + tip;
            int j = (int)(upper_bound(ends.begin(), ends.end(), start) - ends.begin());
            dp[i + 1] = max(dp[i], earn + dp[j]);
        }
        return dp[m];
    }
};
