// LeetCode 2021 - Brightest Position on Street
// https://leetcode.com/problems/brightest-position-on-street/

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
    int brightestPosition(vector<vector<int>>& lights) {
        vector<pair<int,int>> events;
        for (auto& light : lights) {
            int pos = light[0], r = light[1];
            events.push_back({pos - r, 1});
            events.push_back({pos + r + 1, -1});
        }
        sort(events.begin(), events.end(), [](auto& a, auto& b) {
            if (a.first != b.first) return a.first < b.first;
            return a.second > b.second;
        });
        int best = 0, cur = 0, ans = 0;
        for (auto& [x, d] : events) {
            cur += d;
            if (cur > best) { best = cur; ans = x; }
        }
        return ans;
    }
};
