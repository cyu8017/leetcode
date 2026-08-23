// LeetCode 2071 - Maximum Number of Tasks You Can Assign
// https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

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
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        sort(tasks.begin(), tasks.end());
        sort(workers.begin(), workers.end());
        auto can = [&](int k) {
            if (k == 0) return true;
            multiset<int> ws(workers.end() - k, workers.end());
            int p = pills;
            for (int i = k - 1; i >= 0; i--) {
                int task = tasks[i];
                auto it = prev(ws.end());
                if (*it >= task) { ws.erase(it); continue; }
                if (p == 0) return false;
                it = ws.lower_bound(task - strength);
                if (it == ws.end()) return false;
                ws.erase(it);
                p--;
            }
            return true;
        };
        int lo = 0, hi = min((int)tasks.size(), (int)workers.size());
        while (lo < hi) {
            int mid = (lo + hi + 1) / 2;
            if (can(mid)) lo = mid;
            else hi = mid - 1;
        }
        return lo;
    }
};
