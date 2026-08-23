// LeetCode 2184 - Number of Ways to Build Sturdy Brick Wall
// https://leetcode.com/problems/number-of-ways-to-build-sturdy-brick-wall/

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
    int buildWall(int height, int width, vector<int>& bricks) {
        const int MOD = 1000000007;
        vector<int> masks;
        function<void(int,int)> gen = [&](int remain, int mask) {
            if (remain == 0) { masks.push_back(mask); return; }
            for (int b : bricks) {
                if (b <= remain) {
                    int nm = mask;
                    if (remain - b > 0) nm |= 1 << (remain - b);
                    gen(remain - b, nm);
                }
            }
        };
        gen(width, 0);
        int m = masks.size();
        vector<vector<int>> compat(m);
        for (int i = 0; i < m; i++)
            for (int j = 0; j < m; j++)
                if ((masks[i] & masks[j]) == 0) compat[i].push_back(j);
        vector<int> dp(m, 1);
        for (int h = 1; h < height; h++) {
            vector<int> ndp(m);
            for (int i = 0; i < m; i++)
                for (int j : compat[i]) ndp[j] = (ndp[j] + dp[i]) % MOD;
            dp.swap(ndp);
        }
        int ans = 0;
        for (int v : dp) ans = (ans + v) % MOD;
        return ans;
    }
};
