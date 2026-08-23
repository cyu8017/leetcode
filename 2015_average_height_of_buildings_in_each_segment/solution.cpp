// LeetCode 2015 - Average Height of Buildings in Each Segment
// https://leetcode.com/problems/average-height-of-buildings-in-each-segment/

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
    vector<vector<int>> averageHeightOfBuildings(vector<vector<int>>& buildings) {
        vector<array<int,3>> events;
        for (auto& b : buildings) {
            events.push_back({b[0], 1, b[2]});
            events.push_back({b[1], -1, b[2]});
        }
        sort(events.begin(), events.end(), [](auto& a, auto& b) {
            if (a[0] != b[0]) return a[0] < b[0];
            return a[1] < b[1];
        });
        vector<vector<int>> ans;
        int count = 0, sum = 0, prev = events[0][0];
        for (auto& e : events) {
            if (e[0] != prev && count > 0) {
                int avg = sum / count;
                if (!ans.empty() && ans.back()[1] == prev && ans.back()[2] == avg) ans.back()[1] = e[0];
                else ans.push_back({prev, e[0], avg});
            }
            count += e[1];
            sum += e[1] * e[2];
            prev = e[0];
        }
        return ans;
    }
};
