// LeetCode 2019 - The Score of Students Solving Math Expression
// https://leetcode.com/problems/the-score-of-students-solving-math-expression/

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
    int evalCorrect(const string& s) {
        vector<int> nums;
        vector<char> ops;
        for (char c : s) {
            if (c >= '0' && c <= '9') nums.push_back(c - '0');
            else ops.push_back(c);
        }
        vector<int> newNums{nums[0]};
        vector<char> newOps;
        for (int j = 0; j < (int)ops.size(); j++) {
            if (ops[j] == '*') newNums.back() *= nums[j + 1];
            else { newOps.push_back(ops[j]); newNums.push_back(nums[j + 1]); }
        }
        int res = newNums[0];
        for (int j = 0; j < (int)newOps.size(); j++) res += newNums[j + 1];
        return res;
    }
public:
    int scoreOfStudents(string s, vector<int>& answers) {
        int n = (int)s.size();
        int correct = evalCorrect(s);
        vector<vector<unordered_set<int>*>> dp(n, vector<unordered_set<int>*>(n, nullptr));
        function<unordered_set<int>*(int,int)> dfs = [&](int l, int r) -> unordered_set<int>* {
            if (dp[l][r]) return dp[l][r];
            auto* res = new unordered_set<int>();
            if (l == r) { res->insert(s[l] - '0'); dp[l][r] = res; return res; }
            for (int i = l + 1; i < r; i += 2) {
                auto* left = dfs(l, i - 1);
                auto* right = dfs(i + 1, r);
                for (int a : *left) for (int b : *right) {
                    int v = s[i] == '+' ? a + b : a * b;
                    if (v <= 1000) res->insert(v);
                }
            }
            dp[l][r] = res;
            return res;
        };
        auto* possible = dfs(0, n - 1);
        int ans = 0;
        for (int a : answers) {
            if (a == correct) ans += 5;
            else if (possible->count(a)) ans += 2;
        }
        return ans;
    }
};
