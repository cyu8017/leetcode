// LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
// https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

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
    bool possiblyEquals(string s1, string s2) {
        int n = (int)s1.size(), m = (int)s2.size();
        map<tuple<int,int,int>, bool> memo;
        function<bool(int,int,int)> dfs = [&](int i, int j, int diff) {
            auto key = make_tuple(i, j, diff);
            if (memo.count(key)) return memo[key];
            if (i == n && j == m) return memo[key] = (diff == 0);
            bool res = false;
            auto isDigit = [](char c) { return c >= '0' && c <= '9'; };
            if (diff == 0 && i < n && j < m && !isDigit(s1[i]) && !isDigit(s2[j])) {
                if (s1[i] == s2[j]) res = dfs(i + 1, j + 1, 0);
            } else if (diff > 0 && i < n && !isDigit(s1[i])) {
                res = dfs(i + 1, j, diff - 1);
            } else if (diff < 0 && j < m && !isDigit(s2[j])) {
                res = dfs(i, j + 1, diff + 1);
            }
            if (!res && i < n && isDigit(s1[i])) {
                int val = 0;
                for (int p = i; p < n && isDigit(s1[p]); p++) {
                    val = val * 10 + (s1[p] - '0');
                    if (dfs(p + 1, j, diff + val)) { res = true; break; }
                }
            }
            if (!res && j < m && isDigit(s2[j])) {
                int val = 0;
                for (int p = j; p < m && isDigit(s2[p]); p++) {
                    val = val * 10 + (s2[p] - '0');
                    if (dfs(i, p + 1, diff - val)) { res = true; break; }
                }
            }
            return memo[key] = res;
        };
        return dfs(0, 0, 0);
    }
};
