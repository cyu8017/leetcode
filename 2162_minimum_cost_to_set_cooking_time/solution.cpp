// LeetCode 2162 - Minimum Cost to Set Cooking Time
// https://leetcode.com/problems/minimum-cost-to-set-cooking-time/

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
    int minCostSetTime(int startAt, int moveCost, int pushCost, int targetSeconds) {
        auto cost = [&](int mins, int secs) {
            if (mins < 0 || mins > 99 || secs < 0 || secs > 99) return INT_MAX / 2;
            string s;
            if (mins > 0) {
                s = to_string(mins);
                s += char('0' + secs / 10);
                s += char('0' + secs % 10);
            } else s = to_string(secs);
            char cur = '0' + startAt;
            int ans = 0;
            for (char c : s) {
                if (c != cur) { ans += moveCost; cur = c; }
                ans += pushCost;
            }
            return ans;
        };
        int mins = targetSeconds / 60, secs = targetSeconds % 60;
        int ans = cost(mins, secs);
        if (mins > 0) ans = min(ans, cost(mins - 1, secs + 60));
        return ans;
    }
};
