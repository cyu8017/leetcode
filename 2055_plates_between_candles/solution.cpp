// LeetCode 2055 - Plates Between Candles
// https://leetcode.com/problems/plates-between-candles/

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
    vector<int> platesBetweenCandles(string s, vector<vector<int>>& queries) {
        int n = (int)s.size();
        vector<int> pref(n + 1), left(n), right(n);
        int last = -1;
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i] + (s[i] == '*');
            if (s[i] == '|') last = i;
            left[i] = last;
        }
        last = -1;
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == '|') last = i;
            right[i] = last;
        }
        vector<int> ans(queries.size());
        for (int i = 0; i < (int)queries.size(); i++) {
            int l = right[queries[i][0]], r = left[queries[i][1]];
            if (l != -1 && r != -1 && l < r) ans[i] = pref[r] - pref[l];
        }
        return ans;
    }
};
