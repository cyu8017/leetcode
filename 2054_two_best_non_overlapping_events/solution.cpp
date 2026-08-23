// LeetCode 2054 - Two Best Non-Overlapping Events
// https://leetcode.com/problems/two-best-non-overlapping-events/

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
    int maxTwoEvents(vector<vector<int>>& events) {
        sort(events.begin(), events.end());
        int n = (int)events.size();
        vector<int> suffix(n + 1);
        for (int i = n - 1; i >= 0; i--) suffix[i] = max(suffix[i + 1], events[i][2]);
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans = max(ans, events[i][2]);
            int lo = i + 1, hi = n;
            while (lo < hi) {
                int mid = (lo + hi) / 2;
                if (events[mid][0] > events[i][1]) hi = mid;
                else lo = mid + 1;
            }
            if (lo < n) ans = max(ans, events[i][2] + suffix[lo]);
        }
        return ans;
    }
};
