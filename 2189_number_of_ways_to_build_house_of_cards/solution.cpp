// LeetCode 2189 - Number of Ways to Build House of Cards
// https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/

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
    int houseOfCards(int n) {
        vector<int> dp(n + 1);
        dp[0] = 1;
        for (int k = 1; 3 * k - 1 <= n; k++) {
            int cost = 3 * k - 1;
            for (int j = n; j >= cost; j--) dp[j] += dp[j - cost];
        }
        return dp[n];
    }
};
