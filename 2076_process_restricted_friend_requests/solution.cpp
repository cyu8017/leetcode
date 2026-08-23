// LeetCode 2076 - Process Restricted Friend Requests
// https://leetcode.com/problems/process-restricted-friend-requests/

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
    vector<bool> friendRequests(int n, vector<vector<int>>& restrictions, vector<vector<int>>& requests) {
        vector<int> parent(n);
        iota(parent.begin(), parent.end(), 0);
        function<int(int)> find = [&](int x) {
            return parent[x] == x ? x : parent[x] = find(parent[x]);
        };
        auto unite = [&](int a, int b) {
            a = find(a); b = find(b);
            if (a != b) parent[a] = b;
        };
        vector<bool> ans(requests.size());
        for (int i = 0; i < (int)requests.size(); i++) {
            int u = find(requests[i][0]), v = find(requests[i][1]);
            bool ok = true;
            if (u != v) {
                for (auto& r : restrictions) {
                    int x = find(r[0]), y = find(r[1]);
                    if ((x == u && y == v) || (x == v && y == u)) { ok = false; break; }
                }
            }
            ans[i] = ok;
            if (ok) unite(u, v);
        }
        return ans;
    }
};
