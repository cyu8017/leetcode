// LeetCode 2167 - Minimum Time to Remove All Cars Containing Illegal Goods
// https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/

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
    int minimumTime(string s) {
        int n = s.size();
        vector<int> left(n);
        if (s[0] == '1') left[0] = 1;
        for (int i = 1; i < n; i++) {
            left[i] = left[i - 1];
            if (s[i] == '1') left[i] = min(i + 1, left[i - 1] + 2);
        }
        int ans = left[n - 1], right = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (s[i] == '1') right = min(n - i, right + 2);
            int leftCost = i > 0 ? left[i - 1] : 0;
            ans = min(ans, leftCost + right);
        }
        return ans;
    }
};
