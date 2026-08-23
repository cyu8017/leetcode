// LeetCode 2218 - Maximum Value of K Coins From Piles
// https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/

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
    int maxValueOfCoins(vector<vector<int>>& piles, int k) {
        vector<int> dp(k + 1);
        for (auto& pile : piles) {
            vector<int> ndp = dp;
            int sum = 0;
            for (int take = 1; take <= (int)pile.size() && take <= k; take++) {
                sum += pile[take - 1];
                for (int j = take; j <= k; j++)
                    ndp[j] = max(ndp[j], dp[j - take] + sum);
            }
            dp.swap(ndp);
        }
        return dp[k];
    }
};
