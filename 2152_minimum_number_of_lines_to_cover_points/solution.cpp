// LeetCode 2152 - Minimum Number of Lines to Cover Points
// https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/

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
    int minimumLines(vector<vector<int>>& points) {
        int n = points.size();
        if (n <= 2) return 1;
        auto colinear = [&](vector<int>& a, vector<int>& b, vector<int>& c) {
            return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1]);
        };
        int inf = n;
        vector<int> dp(1 << n, inf);
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); mask++) {
            if (dp[mask] == inf) continue;
            int i = 0;
            while (i < n && (mask & (1 << i))) i++;
            if (i == n) continue;
            int nm = mask | (1 << i);
            dp[nm] = min(dp[nm], dp[mask] + 1);
            for (int j = i + 1; j < n; j++) {
                if (mask & (1 << j)) continue;
                nm = mask | (1 << i) | (1 << j);
                for (int k = 0; k < n; k++)
                    if ((nm & (1 << k)) == 0 && colinear(points[i], points[j], points[k]))
                        nm |= 1 << k;
                dp[nm] = min(dp[nm], dp[mask] + 1);
            }
        }
        return dp[(1 << n) - 1];
    }
};
