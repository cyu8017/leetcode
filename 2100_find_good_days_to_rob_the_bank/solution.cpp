// LeetCode 2100 - Find Good Days to Rob the Bank
// https://leetcode.com/problems/find-good-days-to-rob-the-bank/

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
    vector<int> goodDaysToRobBank(vector<int>& security, int time) {
        int n = (int)security.size();
        if (time == 0) {
            vector<int> ans(n);
            iota(ans.begin(), ans.end(), 0);
            return ans;
        }
        vector<int> left(n), right(n);
        for (int i = 1; i < n; i++) if (security[i] <= security[i - 1]) left[i] = left[i - 1] + 1;
        for (int i = n - 2; i >= 0; i--) if (security[i] <= security[i + 1]) right[i] = right[i + 1] + 1;
        vector<int> ans;
        for (int i = time; i < n - time; i++)
            if (left[i] >= time && right[i] >= time) ans.push_back(i);
        return ans;
    }
};
