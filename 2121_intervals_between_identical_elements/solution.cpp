// LeetCode 2121 - Intervals Between Identical Elements
// https://leetcode.com/problems/intervals-between-identical-elements/

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
    vector<long long> getDistances(vector<int>& arr) {
        int n = arr.size();
        unordered_map<int, vector<int>> pos;
        for (int i = 0; i < n; i++) pos[arr[i]].push_back(i);
        vector<long long> ans(n);
        for (auto& [v, idxs] : pos) {
            int m = idxs.size();
            vector<long long> pref(m + 1);
            for (int i = 0; i < m; i++) pref[i + 1] = pref[i] + idxs[i];
            for (int i = 0; i < m; i++) {
                long long left = 1LL * i * idxs[i] - pref[i];
                long long right = (pref[m] - pref[i + 1]) - 1LL * (m - i - 1) * idxs[i];
                ans[idxs[i]] = left + right;
            }
        }
        return ans;
    }
};
