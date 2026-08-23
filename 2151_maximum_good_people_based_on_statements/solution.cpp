// LeetCode 2151 - Maximum Good People Based on Statements
// https://leetcode.com/problems/maximum-good-people-based-on-statements/

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
    int maximumGood(vector<vector<int>>& statements) {
        int n = statements.size(), ans = 0;
        auto ok = [&](int mask) {
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) == 0) continue;
                for (int j = 0; j < n; j++) {
                    int s = statements[i][j];
                    if (s == 2) continue;
                    bool goodJ = mask & (1 << j);
                    if ((s == 1 && !goodJ) || (s == 0 && goodJ)) return false;
                }
            }
            return true;
        };
        for (int mask = 0; mask < (1 << n); mask++)
            if (ok(mask)) ans = max(ans, __builtin_popcount(mask));
        return ans;
    }
};
