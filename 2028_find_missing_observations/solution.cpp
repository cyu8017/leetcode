// LeetCode 2028 - Find Missing Observations
// https://leetcode.com/problems/find-missing-observations/

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
    vector<int> missingRolls(vector<int>& rolls, int mean, int n) {
        int sum = 0;
        for (int r : rolls) sum += r;
        int remain = mean * ((int)rolls.size() + n) - sum;
        if (remain < n || remain > 6 * n) return {};
        vector<int> ans(n, remain / n);
        int extra = remain % n;
        for (int i = 0; i < extra; i++) ans[i]++;
        return ans;
    }
};
